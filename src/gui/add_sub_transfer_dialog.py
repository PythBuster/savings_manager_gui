from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QDialog, QLineEdit, QStyledItemDelegate,
                               QStyleOptionViewItem, QWidget)

from src.gui.ui.ui_add_sub_transfer_amount_dialog import \
    Ui_AddSubTransferAmountDialog


class RightAlignedDelegate(QStyledItemDelegate):
    def initStyleOption(self, option: QStyleOptionViewItem, index):
        super().initStyleOption(option, index)
        option.displayAlignment = (
            Qt.AlignRight | Qt.AlignVCenter
        )  # Right-align the text


class AddSubDialog(QDialog, Ui_AddSubTransferAmountDialog):
    def __init__(
        self,
        parent: QWidget | None = None,
    ):
        super().__init__(parent)
        self.setupUi(self)

        self.pushButton_apply.clicked.connect(self.accept)
        self.pushButton_cancel.clicked.connect(self.reject)
        self.pushButton_apply.setEnabled(False)  # Disable the Apply button
        self.group_to_moneybox.setVisible(False)

        self.adjustSize()

        # Create a right-aligned QLineEdit for the current item display
        line_edit = QLineEdit(self)
        line_edit.setAlignment(Qt.AlignRight)  # Right-align the text in the line edit
        line_edit.setReadOnly(True)  # Prevent manual input
        self.comboBox_moneyboxes.setLineEdit(line_edit)

        # Set the custom delegate for right-aligned text
        delegate = RightAlignedDelegate(self.comboBox_moneyboxes)
        self.comboBox_moneyboxes.setItemDelegate(delegate)

        self._is_amount_valid = False

        self._previous_lineEdit_amount_text = self.lineEdit_amount.text()
        # connections
        self.lineEdit_amount.textChanged.connect(self.validate_amount)

    def validate_amount(self):
        text = self.lineEdit_amount.text().strip()

        # digits only
        if text.count(",") > 1 or text == ",":
            # reset text to previous valid one
            self.lineEdit_amount.blockSignals(True)
            self.lineEdit_amount.setText(self._previous_lineEdit_amount_text)
            self.lineEdit_amount.blockSignals(False)

            if not self._previous_lineEdit_amount_text:
                self._is_amount_valid = False
                self.pushButton_apply.setEnabled(self._is_amount_valid)

            return

        for ch in text:
            if ch.isdigit() or ch == ",":
                continue

            # reset text to previous valid one
            self.lineEdit_amount.blockSignals(True)
            self.lineEdit_amount.setText(self._previous_lineEdit_amount_text)
            self.lineEdit_amount.blockSignals(False)

            if not self._previous_lineEdit_amount_text:
                self._is_amount_valid = False
                self.pushButton_apply.setEnabled(self._is_amount_valid)

            return

        if not text:
            cleaned_text = "0,00"
        else:
            cleaned_text = text.replace(",", "").replace(".", "").lstrip("0") or "0"
            # Formatierung der Eingabe
            while len(cleaned_text) < 3:
                cleaned_text = "0" + cleaned_text
            cleaned_text = f"{cleaned_text[:-2]},{cleaned_text[-2:]}"

        # Setze den Text ohne die TextChanged-Signal erneut auszulösen
        self.lineEdit_amount.blockSignals(True)
        self.lineEdit_amount.setText(cleaned_text)
        self.lineEdit_amount.blockSignals(False)

        # Überprüfe, ob der Betrag gültig ist
        try:
            amount_str = text.replace(",", "").replace(".", "")
            valid = bool(amount_str)

            if valid:
                self._previous_lineEdit_amount_text = cleaned_text
        except ValueError:
            valid = False

        self._is_amount_valid = valid
        self.pushButton_apply.setEnabled(self._is_amount_valid)
