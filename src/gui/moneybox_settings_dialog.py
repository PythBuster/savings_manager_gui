from itertools import count

from PySide6.QtWidgets import QDialog, QWidget

from src.gui.ui.ui_moneybox_settings_dialog import Ui_MoneyboxSettingsDialog


class MoneyboxSettingsDialog(QDialog, Ui_MoneyboxSettingsDialog):
    def __init__(
            self,
            name_label: str = "",
            savings_amount_label: str = "0,00",
            savings_target_label: str = "",
            parent: QWidget|None = None,
):
        super().__init__(parent)
        self.setupUi(self)

        self._is_name_valid = False
        self._is_amount_valid = False
        self._is_target_valid = False

        self.lineEdit_name.setText(name_label)
        self.lineEdit_savings_amount.setText(savings_amount_label)
        self.lineEdit_savings_target.setText(savings_target_label)
        self._previous_lineEdit_savings_amount_text = savings_amount_label
        self._previous_lineEdit_savings_target_text = savings_target_label

        self.validate_name()
        self.validate_amount()
        self.validate_target()

        self.update_apply_button()

        # connections
        self.pushButton_apply.clicked.connect(self.accept)
        self.pushButton_cancel.clicked.connect(self.reject)
        self.lineEdit_name.textChanged.connect(self.validate_name)
        self.lineEdit_savings_amount.textChanged.connect(self.validate_amount)
        self.lineEdit_savings_target.textChanged.connect(self.validate_target)

        self.adjustSize()


    def validate_name(self):
        # Validierung für lineEdit_name: muss mindestens ein Zeichen enthalten
        text = self.lineEdit_name.text().strip()

        self._is_name_valid = len(text) > 0
        self.update_apply_button()

    def validate_amount(self):
        text = self.lineEdit_savings_amount.text().strip()

        # digits only
        if text.count(",") > 1 or text == ",":
            self.lineEdit_savings_amount.blockSignals(True)
            self.lineEdit_savings_amount.setText(self._previous_lineEdit_savings_amount_text)
            self.lineEdit_savings_amount.blockSignals(False)
            self._is_target_valid = False
            return

        for ch in text:
            if ch.isdigit() or ch == ",":
                continue
            else:
                self.lineEdit_savings_amount.blockSignals(True)
                self.lineEdit_savings_amount.setText(self._previous_lineEdit_savings_amount_text)
                self.lineEdit_savings_amount.blockSignals(False)
                self._is_target_valid = False
                return

        if not text:
            cleaned_text = "0,00"
        else:
            cleaned_text = text.replace(",", "").replace(".", "").lstrip('0') or "0"
            # Formatierung der Eingabe
            while len(cleaned_text) < 3:
                cleaned_text = '0' + cleaned_text
            cleaned_text = f"{cleaned_text[:-2]},{cleaned_text[-2:]}"

        # Setze den Text ohne die TextChanged-Signal erneut auszulösen
        self.lineEdit_savings_amount.blockSignals(True)
        self.lineEdit_savings_amount.setText(cleaned_text)
        self.lineEdit_savings_amount.blockSignals(False)

        # Überprüfe, ob der Betrag gültig ist
        try:
            amount_str = text.replace(",", "").replace(".", "")
            valid = bool(amount_str)
        except ValueError:
            valid = False

        self._is_amount_valid = valid
        self.update_apply_button()
        self._previous_lineEdit_savings_amount_text = text

    def validate_target(self):
        text = self.lineEdit_savings_target.text().strip()

        # digits only
        if text.count(",") > 1 or text == ",":
            self.lineEdit_savings_target.blockSignals(True)
            self.lineEdit_savings_target.setText(self._previous_lineEdit_savings_target_text)
            self.lineEdit_savings_target.blockSignals(False)
            self._is_target_valid = False
            return

        for ch in text:
            if ch.isdigit() or ch == ",":
                continue
            else:
                self.lineEdit_savings_target.blockSignals(True)
                self.lineEdit_savings_target.setText(self._previous_lineEdit_savings_target_text)
                self.lineEdit_savings_target.blockSignals(False)
                self._is_target_valid = False
                return

        _prev = self._previous_lineEdit_savings_target_text.replace(",", "").replace(".", "").lstrip('0')

        if text == "0,0" and _prev == "":
            # Setze auf leer, wenn der Text 0,00 ist
            self.lineEdit_savings_target.blockSignals(True)
            self.lineEdit_savings_target.setText("")
            self.lineEdit_savings_target.blockSignals(False)
            self._is_target_valid = True
        else:
            if not text:
                valid = True
            else:
                cleaned_text = text.replace(",", "").replace(".", "").lstrip('0') or "0"

                # Formatierung der Eingabe
                while len(cleaned_text) < 3:
                    cleaned_text = '0' + cleaned_text

                cleaned_text = f"{cleaned_text[:-2]},{cleaned_text[-2:]}"
                # Setze den Text ohne die TextChanged-Signal erneut auszulösen
                self.lineEdit_savings_target.blockSignals(True)
                self.lineEdit_savings_target.setText(cleaned_text)
                self.lineEdit_savings_target.blockSignals(False)

                # Überprüfe, ob der Zielbetrag gültig ist
                try:
                    amount_str = text.replace(",", "").replace(".", "")
                    valid = bool(amount_str)

                    if valid:
                        self._previous_lineEdit_savings_target_text = cleaned_text
                except ValueError:
                    valid = False

            self._is_target_valid = valid

        self.update_apply_button()

    def update_apply_button(self):
        # Aktualisiere den Zustand des Apply-Buttons
        self.pushButton_apply.setEnabled(
            self._is_name_valid and self._is_amount_valid and self._is_target_valid
        )