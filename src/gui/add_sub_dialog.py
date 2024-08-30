import re

from PySide6.QtWidgets import QWidget, QDialog

from src.gui.ui.ui_add_sub_amount_dialog import Ui_AddSubDialog


class AddSubDialog(QDialog, Ui_AddSubDialog):
    def __init__(
            self,
            parent: QWidget|None = None,
    ):
        super().__init__(parent)
        self.setupUi(self)

        self.pushButton_apply.clicked.connect(self.accept)
        self.pushButton_cancel.clicked.connect(self.reject)
        self.pushButton_apply.setEnabled(False)  # Disable the Apply button

        self.adjustSize()

        # connections
        self.lineEdit_amount.textChanged.connect(self.validate_input)

    def validate_input(self):
        # Get the current text from the QLineEdit
        text = self.lineEdit_amount.text()

        # Remove any commas or leading zeros for processing
        cleaned_text = text.replace(",", "").lstrip('0')

        if len(cleaned_text) == 0:
            cleaned_text = "0"  # Set to "0" if the input is empty after cleaning

        # Add leading zeros if necessary to ensure at least 3 digits
        while len(cleaned_text) < 3:
            cleaned_text = '0' + cleaned_text

        # Insert the comma before the last two digits
        formatted_text = f"{cleaned_text[:-2]},{cleaned_text[-2:]}"

        # Update the QLineEdit text without emitting another textChanged signal
        self.lineEdit_amount.blockSignals(True)
        self.lineEdit_amount.setText(formatted_text)
        self.lineEdit_amount.blockSignals(False)

        # Enable the Apply button only if the amount is greater than 0,00 (0 cents)
        amount = int(cleaned_text.replace(",", "").replace(".", ""))
        self.pushButton_apply.setEnabled(amount > 0)

