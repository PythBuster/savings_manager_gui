from PySide6.QtWidgets import QDialog, QWidget

from src.gui.ui.ui_server_settings_dialog import Ui_ServerSettingsDialog


class ServerSettingsDialog(QDialog, Ui_ServerSettingsDialog):
    def __init__(
        self,
        host_label: str,
        port_label: str,
        parent: QWidget | None = None,
    ):
        super().__init__(parent)
        self.setupUi(self)

        self._is_host_valid = False
        self._is_port_valid = False

        self.lineEdit_host.setText(host_label)
        self.lineEdit_port.setText(port_label)

        self._previous_lineEdit_host_text = host_label
        self._previous_lineEdit_port_text = port_label

        self.validate_host()
        self.validate_port()

        self.update_apply_button()

        # connections
        self.pushButton_apply.clicked.connect(self.accept)
        self.pushButton_cancel.clicked.connect(self.reject)
        self.lineEdit_host.textChanged.connect(self.validate_host)
        self.lineEdit_port.textChanged.connect(self.validate_port)

        self.adjustSize()

    def validate_host(self):
        text = self.lineEdit_host.text().strip()
        self._is_host_valid = len(text) > 0
        self.update_apply_button()

    def validate_port(self):
        text = self.lineEdit_port.text().strip()

        # allow digits only
        for ch in text:
            if ch.isdigit():
                continue

            self._is_port_valid = False
            # reset text to previous valid one
            self.lineEdit_savings_amount.blockSignals(True)
            self.lineEdit_savings_amount.setText(
                self._previous_lineEdit_savings_amount_text
            )
            self.lineEdit_savings_amount.blockSignals(False)
            self.update_apply_button()
            return

        if 1 < len(text) > 5:
            self._is_port_valid = False
            # reset text to previous valid one
            self.lineEdit_savings_amount.blockSignals(True)
            self.lineEdit_savings_amount.setText(
                self._previous_lineEdit_savings_amount_text
            )
            self.lineEdit_savings_amount.blockSignals(False)
            self.update_apply_button()
            return

        self._is_port_valid = True
        self.update_apply_button()


    def update_apply_button(self):
        # Aktualisiere den Zustand des Apply-Buttons
        self.pushButton_apply.setEnabled(
            self._is_host_valid and self._is_port_valid
        )
