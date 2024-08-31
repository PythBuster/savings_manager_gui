from pydantic import BaseModel, EmailStr
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QMessageBox, QWidget

from src.gui.ui.ui_app_settings_dialog import Ui_AppSettingsDialog


class UserModel(BaseModel):
    email: EmailStr


class AppSettingsDialog(QDialog, Ui_AppSettingsDialog):
    def __init__(
        self,
        savings_amount_label: str,
        enable_automated_savings: bool,
        send_reports_via_email: bool,
        user_email_address: str,
        overflow_moneybox_mode: str,
        parent: QWidget | None = None,
    ):
        super().__init__(parent)
        self.setupUi(self)

        self.sending_testemail_requested = False
        self._is_amount_valid = False
        self._is_email_address_valid = False

        self.lineEdit_savings_amount.setText(savings_amount_label)
        self._previous_lineEdit_savings_amount_text = savings_amount_label
        self.lineEdit_user_email_address.setText(user_email_address)
        self._previous_lineEdit_user_email_address_text = user_email_address
        self.checkBox_send_reports_via_email.setChecked(send_reports_via_email)
        self.checkBox_enable_automated_savings.setChecked(enable_automated_savings)

        # Finde den Index des Items in der ComboBox
        index = self.comboBox_overflow_moneybox_modes.findText(overflow_moneybox_mode)

        # Wenn der Text gefunden wurde, setze ihn als ausgewähltes Item
        if index != -1:
            self.comboBox_overflow_moneybox_modes.setCurrentIndex(index)
        else:
            raise ValueError("Not allowed overflow moneybox mode.")

        self.validate_email_address()
        self.validate_amount()

        self.update_apply_button()

        # connections
        self.pushButton_apply.clicked.connect(self.accept)
        self.pushButton_cancel.clicked.connect(self.reject)
        self.pushButton_send_testemail.clicked.connect(self.close_with_email_send)
        self.lineEdit_savings_amount.textChanged.connect(self.validate_amount)
        self.lineEdit_user_email_address.textChanged.connect(
            self.validate_email_address
        )
        self.checkBox_send_reports_via_email.stateChanged.connect(
            self.handle_checkbox_state_change
        )
        self.adjustSize()
        self.pushButton_cancel.setFocus()

    def close_with_email_send(self):
        self.sending_testemail_requested = True
        self.accept()

    def handle_checkbox_state_change(self, state):
        if state == Qt.Checked.value:
            self.validate_email_address()
            if not self._is_email_address_valid:
                self.checkBox_send_reports_via_email.setChecked(False)
                QMessageBox.warning(
                    self,
                    "Invalid Email",
                    "The user email is invalid. Please set a valid user email first.",
                )

    def validate_email_address(self):
        if not self.checkBox_send_reports_via_email.isChecked():
            self._is_email_address_valid = True
            self.update_apply_button()
            return

        text = self.lineEdit_user_email_address.text().strip()

        try:
            UserModel(email=text)
            self._is_email_address_valid = True
        except:
            self._is_email_address_valid = False

        self.update_apply_button()

    def validate_amount(self):
        text = self.lineEdit_savings_amount.text().strip()

        # digits only
        if text.count(",") > 1 or text == ",":
            # reset text to previous valid one
            self.lineEdit_savings_amount.blockSignals(True)
            self.lineEdit_savings_amount.setText(
                self._previous_lineEdit_savings_amount_text
            )
            self.lineEdit_savings_amount.blockSignals(False)
            return

        for ch in text:
            if ch.isdigit() or ch == ",":
                continue

            # reset text to previous valid one
            self.lineEdit_savings_amount.blockSignals(True)
            self.lineEdit_savings_amount.setText(
                self._previous_lineEdit_savings_amount_text
            )
            self.lineEdit_savings_amount.blockSignals(False)
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
        self.lineEdit_savings_amount.blockSignals(True)
        self.lineEdit_savings_amount.setText(cleaned_text)
        self.lineEdit_savings_amount.blockSignals(False)

        # Überprüfe, ob der Betrag gültig ist
        try:
            amount_str = text.replace(",", "").replace(".", "")
            valid = bool(amount_str)

            if valid:
                self._previous_lineEdit_savings_target_text = cleaned_text
        except ValueError:
            valid = False

        self._is_amount_valid = valid
        self.update_apply_button()

    def update_apply_button(self):
        # Aktualisiere den Zustand des Apply-Buttons
        self.pushButton_apply.setEnabled(
            self._is_email_address_valid and self._is_amount_valid
        )
