import asyncio
import json

from PySide6.QtWidgets import (QDialog, QMainWindow, QMessageBox, QPushButton,
                               QWidget)
from qasync import asyncSlot
from savings_manager_cli.api_consumers import (GetAppSettingsApiConsumer,
                                               GetMoneyboxesApiConsumer,
                                               PostMoneyboxApiConsumer)

from src.gui.app_data_overview_widget import AppDataOverviewWidget
from src.gui.moneybox_settings_dialog import MoneyboxSettingsDialog
from src.gui.moneybox_widget import MoneyboxWidget
from src.gui.ui.ui_moneyboxes_overview_widget import \
    Ui_MoneyboxesOverviewWidget


class MoneyboxesOverviewWidget(QWidget, Ui_MoneyboxesOverviewWidget):
    def __init__(
        self,
        parent_window: QMainWindow = None,
        parent: QWidget | None = None,
    ):
        self.moneyboxes = None
        self.parent_window = parent_window
        super().__init__(parent)
        self.setupUi(self)

    async def _refresh_app_data_overview_widget(self):
        while self.verticalLayout_app_data_overview.count() > 0:
            item = self.verticalLayout_app_data_overview.takeAt(0)
            widget = item.widget()

            if widget is not None:
                widget.deleteLater()

        async with GetAppSettingsApiConsumer() as consumer:
            if consumer.response.status_code == 200:
                app_settings = consumer.response.json()
            else:
                message_str = consumer.response.content.decode(encoding="utf-8")
                message = json.loads(message_str)["message"]
                QMessageBox.warning(
                    self,
                    "Loading app settings failed",
                    message,
                )
                return

        # TODO collect data

        savings_amount_label = (
            f"{app_settings['savingsAmount'] / 100:.2f} €"
            if app_settings['savingsAmount'] > 0
            else "0.00 €"
        )
        enabled_automated_savings = app_settings["isAutomatedSavingActive"]
        allocated_savings = sum(
            moneybox["savingsAmount"] for moneybox in self.moneyboxes
        )
        allocated_savings_label = (
            f"{allocated_savings / 100:.2f} €"
            if allocated_savings > 0
            else "0.00 €"
        )

        not_allocated_savings = (
            diff
            if (diff := app_settings["savingsAmount"] - allocated_savings) >= 0
            else 0
        )
        not_allocated_savings_label = (
            f"{not_allocated_savings / 100:.2f} €"
            if not_allocated_savings > 0
            else "0.00 €"
        )

        total_balance = sum(moneybox["balance"] for moneybox in self.moneyboxes)

        total_balance_label = (
            f"{total_balance/ 100:.2f} €"
            if total_balance > 0
            else "0.00 €"
        )

        self.verticalLayout_app_data_overview.addWidget(
            AppDataOverviewWidget(
                savings_amount_label=savings_amount_label,
                enabled_automated_savings=enabled_automated_savings,
                allocated_savings_label=allocated_savings_label,
                not_allocated_savings_label=not_allocated_savings_label,
                total_balance_label=total_balance_label,
            )
        )

    async def load_api_content(self):
        """Load API Consumer specific content"""

        async with GetMoneyboxesApiConsumer() as consumer:
            if consumer.response.status_code == 200:
                moneyboxes = consumer.response.json()["moneyboxes"]
            else:
                message_str = consumer.response.content.decode(encoding="utf-8")
                message = json.loads(message_str)["message"]
                QMessageBox.warning(
                    self,
                    "Transfer failed",
                    message,
                )
                return

            priority_sorted_moneyboxes = sorted(
                moneyboxes, key=lambda moneybox: moneybox["priority"]
            )

            self.moneyboxes = priority_sorted_moneyboxes

            max_col_index = 0
            row_index = 0
            i = 0

            for i, moneybox in enumerate(priority_sorted_moneyboxes[1:]):
                row_index = i // 4
                col_index = i % 4

                savings_amount_label = (
                    f"{moneybox['savingsAmount'] / 100:.2f} €"
                    if moneybox['savingsAmount'] > 0
                    else "0.00 €"
                )

                match moneybox["savingsTarget"]:
                    case 0:
                        savings_target_label = "0.00 €"
                    case None:
                        savings_target_label = "No Limit"
                    case _:
                        savings_target_label = f"{moneybox['savingsTarget'] / 100:.2f} €"

                if moneybox["balance"] > 0:
                    balance_label = f"{moneybox['balance'] / 100:.2f} €"
                else:
                    balance_label = "0.00 €"

                moneybox_widget = MoneyboxWidget(
                    moneybox_id=moneybox["id"],
                    name_label=moneybox["name"],
                    savings_amount_label=savings_amount_label,
                    savings_target_label=savings_target_label,
                    balance_label=balance_label,
                    priority_label=str(moneybox["priority"]),
                )
                moneybox_widget.enter_moneybox.connect(
                    self.parent_window.on_enter_moneybox
                )

                self.gridLayout_moneyboxes.addWidget(
                    moneybox_widget,
                    row_index,
                    col_index,
                )

                max_col_index = max(max_col_index, col_index)

            add_new_moneybox_button = QPushButton("+\n\nAdd new\nMoneybox")
            add_new_moneybox_button.setStyleSheet(
                "QPushButton {"
                "    width: 100%;"
                "    height: 100%;"
                "    border-radius: 15px;"  # Radius für runden Button
                "    border: 2px outset #456;"  # Standard-Rahmen
                "    border-color: green;"  # Rahmenfarbe
                "    background-color: #f0f0f0;"  # Hintergrundfarbe
                "    text-align: center;"  # Textzentrierung
                "    font-size: 12pt;"
                "    color: navy;"
                "}"
                "QPushButton:hover {"
                "    background-color: #66bb6a;"  # Saftiges Grün bei Hover
                "    border: 2px solid #2e7d32;"  # Rahmenfarbe bei Hover (dunkles Grün)
                "}"
                "QPushButton:pressed {"
                "    background-color: #a5d6a7;"  # Hintergrundfarbe bei gedrückt (mittelgrün)
                "    border: 2px inset #1b5e20;"  # Rahmenfarbe bei gedrückt (dunkleres Grün)
                "}"
            )

            add_new_moneybox_button.clicked.connect(
                lambda: asyncio.ensure_future(self.on_new_moneybox_clicked()),
            )

            i += 1
            row_index = i // 4
            col_index = i % 4

            self.gridLayout_moneyboxes.addWidget(
                add_new_moneybox_button,
                row_index,
                col_index,
            )

            col_span = max(0, max_col_index) + 1
            row = max(0, row_index) + 1

            savings_amount_label = (
                f"{priority_sorted_moneyboxes[0]['savingsAmount'] / 100:.2f} €"
                if priority_sorted_moneyboxes[0]['savingsAmount'] > 0
                else "0.00 €"
            )

            savings_target = priority_sorted_moneyboxes[0]['savingsTarget']
            match savings_target:
                case 0:
                    savings_target_label = "0.00 €"
                case None:
                    savings_target_label = "No Limit"
                case _:
                    savings_target_label = f"{savings_target / 100:.2f} €"

            if priority_sorted_moneyboxes[0]['balance'] > 0:
                balance_label = f"{priority_sorted_moneyboxes[0]['balance'] / 100:.2f} €"
            else:
                balance_label = "0.00 €"

            moneybox_widget = MoneyboxWidget(
                moneybox_id=priority_sorted_moneyboxes[0]["id"],
                name_label=priority_sorted_moneyboxes[0]["name"],
                savings_amount_label=savings_amount_label,
                savings_target_label=savings_target_label,
                balance_label=balance_label,
                priority_label=str(priority_sorted_moneyboxes[0]["priority"]),
            )
            moneybox_widget.enter_moneybox.connect(self.parent_window.on_enter_moneybox)

            self.gridLayout_moneyboxes.addWidget(
                moneybox_widget,
                row,
                0,
                1,
                col_span,
            )

        await self._refresh_app_data_overview_widget()

    @asyncSlot()
    async def on_new_moneybox_clicked(self):
        dialog = MoneyboxSettingsDialog()
        dialog.setWindowTitle("Create moneybox...")

        result = dialog.exec()

        if result == QDialog.Accepted:
            name = dialog.lineEdit_name.text()
            savings_amount = int(
                dialog.lineEdit_savings_amount.text().replace(",", "").replace(".", "")
            )
            savings_target = (
                dialog.lineEdit_savings_target.text().replace(",", "").replace(".", "")
            )

            if savings_target:
                consumer = PostMoneyboxApiConsumer(
                    name=name,
                    savings_amount=savings_amount,
                    savings_target=int(savings_target),
                )
            else:
                consumer = PostMoneyboxApiConsumer(
                    name=name,
                    savings_amount=savings_amount,
                    savings_target=None,
                )

            async with consumer:
                if consumer.response.status_code == 200:
                    QMessageBox.information(
                        self,
                        "Created moneybox",
                        "Created moneybox successfully!",
                    )
                    await self.parent_window.load_moneyboxes_overview_widget()
                else:
                    message_str = consumer.response.content.decode(encoding="utf-8")
                    message = json.loads(message_str)["message"]
                    QMessageBox.warning(
                        self,
                        "Creation failed",
                        f"{message} (Amounts are expressed in cents.)",
                    )
