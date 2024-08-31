from PySide6.QtWidgets import QWidget

from src.gui.ui.ui_app_data_overview_widget import Ui_AppDataOverviewWidget


class AppDataOverviewWidget(QWidget, Ui_AppDataOverviewWidget):
    def __init__(
        self,
        savings_amount_label: str,
        enabled_automated_savings: bool,
        allocated_savings_label: str,
        not_allocated_savings_label: str,
        total_balance_label: str,
        parent: QWidget | None = None,
    ):
        enabled_automated_label = "Enabled" if enabled_automated_savings else "Disabled"

        super().__init__(parent)
        self.setupUi(self)

        self.label_savings_amount.setText(savings_amount_label)
        self.label_automated_savings_active_state.setText(enabled_automated_label)
        self.label_allocated_savings.setText(allocated_savings_label)
        self.label_not_allocated_savings.setText(not_allocated_savings_label)
        self.label_total_balance.setText(total_balance_label)

        self.adjustSize()
