import asyncio
from typing import Any

from PySide6.QtCore import Signal, Qt
from PySide6.QtWidgets import QWidget, QDialog, QMessageBox, QStyledItemDelegate, QStyleOptionViewItem
from qasync import asyncSlot

from savings_manager_cli.api_consumers import PostMoneyboxBalanceAddApiConsumer, PostMoneyboxBalanceSubApiConsumer, \
    GetMoneyboxesApiConsumer, PostMoneyboxBalanceTransferApiConsumer

from src.gui.add_sub_transfer_dialog import AddSubDialog
from src.gui.ui.ui_moneybox_overview_widget import Ui_MoneyboxOverviewWidget




class MoneyboxOverviewWidget(QWidget, Ui_MoneyboxOverviewWidget):
    add_amount_clicked = Signal(int)
    sub_amount_clicked = Signal(int)
    transfer_amount_clicked = Signal(int)

    def __init__(
            self,
            moneybox_id: int,
            name_label: str,
            priority_label: str,
            savings_amount_label: str,
            savings_target_label: str,
            balance_label: str,
            parent: QWidget|None = None,
    ):
        self.moneybox_id = moneybox_id

        super().__init__(parent)
        self.setupUi(self)

        self.update_data(
            {
                "name_label": name_label,
                "priority_label": priority_label,
                "savings_amount_label": savings_amount_label,
                "savings_target_label": savings_target_label,
                "balance_label": balance_label,
            }
        )
        # connections
        self.pushButton_add_amount.clicked.connect(
            lambda: asyncio.ensure_future(self.on_add_amount_clicked())
        )
        self.pushButton_sub_amount.clicked.connect(
            lambda: asyncio.ensure_future(self.on_sub_amount_clicked())
        )
        self.pushButton_transfer_amount.clicked.connect(
            lambda: asyncio.ensure_future(self.on_transfer_amount_clicked())
        )

        self.adjustSize()

    def update_data(self, data: dict[str, Any]):
        self.label_id.setText(str(self.moneybox_id))
        self.label_name.setText(data["name_label"])
        self.label_balance.setText(data["balance_label"])
        self.label_savings_amount.setText(data["savings_amount_label"])
        self.label_savings_target.setText(data["savings_target_label"])
        self.label_priority.setText(data["priority_label"])

    @asyncSlot()
    async def on_add_amount_clicked(self):
        dialog = AddSubDialog()
        dialog.setWindowTitle("Add amount...")

        result = dialog.exec()

        if result == QDialog.Accepted:
            amount = int(dialog.lineEdit_amount.text().replace(",", "").replace(".", ""))
            description = dialog.lineEdit_description.text()

            async with PostMoneyboxBalanceAddApiConsumer(
                moneybox_id=self.moneybox_id,
                amount=amount,
                description=description
            ) as consumer:
                if consumer.response.status_code == 200:
                    QMessageBox.information(
                        self,
                        "Added amount",
                        "Added amount successfully!",
                    )

                    data = consumer.response.json()
                    self.update_data(
                        {
                            "moneybox_id": self.moneybox_id,
                            "name_label": data["name"],
                            "priority_label": str(data["priority"]),
                            "savings_amount_label": (
                                f"{data['savings_amount'] / 100:.2f} €".replace(".", ",")
                            ),
                            "savings_target_label": (
                                "No Limit"
                                if data["savings_target"] is None
                                else f"{data['savings_target'] / 100:.2f} €".replace(".", ",")
                            ),
                            "balance_label": (
                                f"{data['balance'] / 100:.2f} €".replace(".", ",")
                            ),
                        }
                    )

    @asyncSlot()
    async def on_sub_amount_clicked(self):
        dialog = AddSubDialog()
        dialog.setWindowTitle("Add amount...")

        result = dialog.exec()

        if result == QDialog.Accepted:
            amount = int(dialog.lineEdit_amount.text().replace(",", "").replace(".", ""))
            description = dialog.lineEdit_description.text()

            async with PostMoneyboxBalanceSubApiConsumer(
                    moneybox_id=self.moneybox_id,
                    amount=amount,
                    description=description
            ) as consumer:
                if consumer.response.status_code == 200:
                    QMessageBox.information(
                        self,
                        "Subbed amount",
                        "Subbed amount successfully!",
                    )

                    data = consumer.response.json()
                    self.update_data(
                        {
                            "moneybox_id": self.moneybox_id,
                            "name_label": data["name"],
                            "priority_label": str(data["priority"]),
                            "savings_amount_label": (
                                f"{data['savings_amount'] / 100:.2f} €".replace(".", ",")
                            ),
                            "savings_target_label": (
                                "No Limit"
                                if data["savings_target"] is None
                                else f"{data['savings_target'] / 100:.2f} €".replace(".", ",")
                            ),
                            "balance_label": (
                                f"{data['balance'] / 100:.2f} €".replace(".", ",")
                            ),
                        }
                    )

    @asyncSlot()
    async def on_transfer_amount_clicked(self):
        dialog = AddSubDialog()
        dialog.setWindowTitle("Transfert amount...")

        # fill combobox with moneybox names and ids
        async with GetMoneyboxesApiConsumer() as consumer:
            if consumer.response.status_code == 200:
                moneyboxes = consumer.response.json()["moneyboxes"]
                sorted_by_priority_moneyboxes = sorted(moneyboxes, key=lambda m: m["priority"])

                for moneybox in sorted_by_priority_moneyboxes:
                    if self.moneybox_id != moneybox["id"]:
                        dialog.comboBox_moneyboxes.addItem(f"{moneybox['name']} (ID: {moneybox['id']})")
            else:
                # TODO: inform user about erros
                return

        dialog.group_to_moneybox.setVisible(True)

        result = dialog.exec()

        if result == QDialog.Accepted:
            amount = int(dialog.lineEdit_amount.text().replace(",", "").replace(".", ""))
            description = dialog.lineEdit_description.text()
            to_moneybox_id = int(dialog.comboBox_moneyboxes.currentText().split(":")[-1][:-1].strip())

            async with PostMoneyboxBalanceTransferApiConsumer(
                    from_moneybox_id=self.moneybox_id,
                    to_moneybox_id=to_moneybox_id,
                    amount=amount,
                    description=description
            ) as consumer:
                if consumer.response.status_code == 204:
                    QMessageBox.information(
                        self,
                        "Transferred amount",
                        "Transferred amount successfully!",
                    )

                    new_balance = int(self.label_balance.text().replace(",", "").replace(".", "").replace("€", "").strip()) - amount
                    self.label_balance.setText(
                        f"{new_balance / 100:.2f} €".replace(".", ",")
                    )
