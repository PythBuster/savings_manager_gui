from PySide6.QtWidgets import QWidget, QPushButton
from savings_manager_cli.api_consumers import GetMoneyboxesApiConsumer

from src.gui.ui.ui_moneyboxes_overview_widget import Ui_MoneyboxesOverviewWidget


class MoneyboxesOverviewWidget(QWidget, Ui_MoneyboxesOverviewWidget):
    def __init__(self, parent: QWidget|None = None):
        super().__init__(parent)
        self.setupUi(self)

    async def load_api_content(self, *args, **kwargs):
        """Load API Consumer specific content"""

        async with GetMoneyboxesApiConsumer() as consumer:
            if consumer.response.status_code == 200:
                moneyboxes = consumer.response.json()["moneyboxes"]
            else:
                moneyboxes = []

            priority_sorted_moneyboxes = sorted(moneyboxes, key=lambda moneybox: moneybox["priority"])

            max_col_index = 0
            row_index = 0

            for i, moneybox in enumerate(priority_sorted_moneyboxes[1:]):
                row_index = i // 4
                col_index = i % 4
                self.gridLayout_moneyboxes.addWidget(
                    QPushButton(moneybox["name"]),
                    row_index,
                    col_index,
                )

                max_col_index = max(max_col_index, col_index)

            col_span = max(0, max_col_index) + 1
            row = max(0, row_index) + 1

            self.gridLayout_moneyboxes.addWidget(
                QPushButton(priority_sorted_moneyboxes[0]["name"]),
                row,
                0,
                1,
                col_span,
            )






