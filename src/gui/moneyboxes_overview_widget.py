from PySide6.QtWidgets import QWidget

from src.gui.ui.ui_moneyboxes_overview_widget import Ui_MoneyboxesOverviewWidget


class MoneyboxesOverviewWidget(QWidget, Ui_MoneyboxesOverviewWidget):
    def __init__(self, parent: QWidget|None = None):
        super().__init__(parent)
        self.setupUi(self)


