from PySide6.QtWidgets import QWidget, QPushButton, QMainWindow
from savings_manager_cli.api_consumers import GetMoneyboxesApiConsumer

from src.gui.moneybox_widget import MoneyboxWidget
from src.gui.ui.ui_moneyboxes_overview_widget import Ui_MoneyboxesOverviewWidget


class MoneyboxesOverviewWidget(QWidget, Ui_MoneyboxesOverviewWidget):
    def __init__(
            self,
            parent_window: QMainWindow = None,
            parent: QWidget|None = None,
    ):
        self.parent_window = parent_window
        super().__init__(parent)
        self.setupUi(self)

    async def load_api_content(self, *args, **kwargs):
        """Load API Consumer specific content"""

        async with GetMoneyboxesApiConsumer() as consumer:
            if consumer.response.status_code == 200:
                moneyboxes = consumer.response.json()["moneyboxes"]
            else:
                # TODO: show error? label? like: No Data ...
                return

            priority_sorted_moneyboxes = sorted(moneyboxes, key=lambda moneybox: moneybox["priority"])

            max_col_index = 0
            row_index = 0

            for i, moneybox in enumerate(priority_sorted_moneyboxes[1:]):
                row_index = i // 4
                col_index = i % 4

                moneybox_widget = MoneyboxWidget(
                    moneybox_id=moneybox["id"],
                    name_label=moneybox["name"],
                    savings_amount_label=f"{moneybox['savings_amount'] / 100:.2f} €".replace(".", ","),
                    savings_target_label=(
                        "No Limit"
                        if moneybox["savings_target"] is None
                        else f"{moneybox['savings_target'] / 100:.2f} €".replace(".", ",")
                    ),
                    balance_label=f"{moneybox['balance'] / 100:.2f} €".replace(".", ","),
                    priority_label=str(moneybox["priority"]),
                )
                moneybox_widget.enter_moneybox.connect(self.parent_window.on_enter_moneybox)

                self.gridLayout_moneyboxes.addWidget(
                    moneybox_widget,
                    row_index,
                    col_index,
                )

                max_col_index = max(max_col_index, col_index)

            col_span = max(0, max_col_index) + 1
            row = max(0, row_index) + 1

            moneybox_widget = MoneyboxWidget(
                moneybox_id=moneybox["id"],
                name_label=priority_sorted_moneyboxes[0]["name"],
                savings_amount_label=(
                    f"{priority_sorted_moneyboxes[0]['savings_amount'] / 100:.2f} €".replace(".", ",")
                ),
                savings_target_label=(
                    "No Limit"
                    if priority_sorted_moneyboxes[0]["savings_target"] is None
                    else f"{priority_sorted_moneyboxes[0]['savings_target'] / 100:.2f} €".replace(".", ",")
                ),
                balance_label=f"{priority_sorted_moneyboxes[0]['balance'] / 100:.2f} €".replace(".", ","),
                priority_label="",
            )
            moneybox_widget.enter_moneybox.connect(self.parent_window.on_enter_moneybox)

            self.gridLayout_moneyboxes.addWidget(
                moneybox_widget,
                row,
                0,
                1,
                col_span,
            )
