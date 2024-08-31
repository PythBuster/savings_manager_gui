from PySide6.QtCore import Signal
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import QWidget

from src.gui.ui.ui_moneybox_widget import Ui_MoneyBoxWidget


class MoneyboxWidget(QWidget, Ui_MoneyBoxWidget):
    enter_moneybox = Signal(int)

    def __init__(
        self,
        moneybox_id: int,
        name_label: str,
        priority_label: str,
        savings_amount_label: str,
        savings_target_label: str,
        balance_label: str,
        parent: QWidget | None = None,
    ):
        self.moneybox_id = moneybox_id

        super().__init__(parent)
        self.setupUi(self)

        self.label_id.setText(str(moneybox_id))
        self.label_name.setText(name_label)
        self.label_priority.setText(priority_label)
        self.label_savings_amount.setText(savings_amount_label)
        self.label_target_amount.setText(savings_target_label)
        self.label_balance.setText(balance_label)

        if priority_label == "0":  # is overflow moneybox
            self.label_priority.setVisible(False)
            self.label_savings_amount.setVisible(False)
            self.label_target_amount.setVisible(False)
            self.label_target_title.setVisible(False)
            self.label_savings_amount_prefix.setVisible(False)

        self.adjustSize()

    def mousePressEvent(self, event: QMouseEvent):
        self.enter_moneybox.emit(self.moneybox_id)
        super().mousePressEvent(event)
