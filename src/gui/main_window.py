import asyncio
import json

from PySide6.QtCore import QSettings, QByteArray
from PySide6.QtWidgets import (QDialog, QMainWindow, QMessageBox,
                               QWidget)
from qasync import asyncClose, asyncSlot
from savings_manager_cli import api_consumers
from savings_manager_cli.api_consumers import (GetAppSettingsApiConsumer,
                                               GetMoneyboxApiConsumer,
                                               PatchAppSettingsApiConsumer)

from src.gui.app_settings_dialog import AppSettingsDialog
from src.gui.moneybox_overview_widget import MoneyboxOverviewWidget
from src.gui.moneyboxes_overview_widget import MoneyboxesOverviewWidget
from src.gui.prioritylist_widget import PrioritylistWidget
from src.gui.server_settings_dialog import ServerSettingsDialog
from src.gui.ui.ui_main_window import Ui_MainWindow
from src.utils import get_app_data


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)
        self.setupUi(self)

        # read all settings
        self.read_server_settings()

        app_data = get_app_data()
        app_title = f"Savings Manager GUI v{app_data['version']}"
        self.setWindowTitle(app_title)

        # connections
        self.actionAbout_Qt.triggered.connect(
            lambda: QMessageBox.aboutQt(self, "About Qt")
        )
        self.actionAbout_Savings_Manager_GUI.triggered.connect(
            lambda: QMessageBox.about(self, f"About {app_title}", "...")
        )
        self.action_Settings.triggered.connect(
            lambda: asyncio.ensure_future(self.on_action_settings_triggered())
        )
        # connection - navigation buttons
        self.pushButton_MoneyboxesOverview.clicked.connect(
            lambda: asyncio.ensure_future(self.load_moneyboxes_overview_widget())
        )
        self.pushButton_PrioritylistWidget.clicked.connect(
            lambda: asyncio.ensure_future(self.load_prioritylist_widget())
        )
        self.pushButton_AppSettingsWidget.clicked.connect(
            lambda: asyncio.ensure_future(self.load_app_settings_widget())
        )

    @asyncSlot()
    async def on_action_settings_triggered(self):
        server_settings_dialog = ServerSettingsDialog(
            host_label=api_consumers.BASE_URL,
            port_label=str(api_consumers.PORT),
        )

        result = server_settings_dialog.exec()

        if result == QDialog.Accepted:
            new_host = server_settings_dialog.lineEdit_host.text()
            new_port = int(server_settings_dialog.lineEdit_port.text())

            api_consumers.BASE_URL = new_host
            api_consumers.PORT = new_port

            self.write_server_ettings()

            QMessageBox.information(
                self,
                "Updated server settings.",
                "Updated server settings successfully.",
            )

    @asyncSlot()
    async def on_enter_moneybox(self, moneybox_id: int):
        await self.load_moneybox_overview_widget(moneybox_id=moneybox_id)

    def write_server_ettings(self):
        settings = QSettings("PythBuster", "SavingsManager")

        settings.beginGroup("MainWindow")
        settings.setValue(
            "server_settings",
            {
                "host": api_consumers.BASE_URL,
                "port": api_consumers.PORT,
            },
        )

        settings.endGroup()

    def read_server_settings(self):
        settings = QSettings("PythBuster", "SavingsManager")

        settings.beginGroup("MainWindow")
        server_settings = settings.value("server_settings")

        if server_settings is not None:
            api_consumers.BASE_URL = server_settings["host"]
            api_consumers.PORT = server_settings["port"]

        settings.endGroup()

    async def load_prioritylist_widget(self):
        prioritylist_widget = PrioritylistWidget(parent_window=self)
        await self.switch_main_board_widget(child=prioritylist_widget)

    async def load_app_settings_widget(self):
        async with GetAppSettingsApiConsumer() as consumer:
            if consumer.response.status_code == 200:
                data = consumer.response.json()

                match data["overflow_moneybox_automated_savings_mode"]:
                    case "collect":
                        mode = "collect"
                    case "add_to_automated_savings_amount":
                        mode = "add"
                    case "fill_up_limited_moneyboxes":
                        mode = "fill"
                    case _:
                        raise ValueError(
                            f"No supported {data['overflow_moneybox_automated_savings_mode']}"
                        )

                app_settings_dialog = AppSettingsDialog(
                    savings_amount_label=(
                        f"{data['savings_amount'] / 100:.2f}".replace(".", ",")
                    ),
                    enable_automated_savings=data["is_automated_saving_active"],
                    send_reports_via_email=data["send_reports_via_email"],
                    user_email_address=data["user_email_address"],
                    overflow_moneybox_mode=mode,
                )

                result = app_settings_dialog.exec()

                if result == QDialog.Accepted:
                    savings_amount_str = (
                        app_settings_dialog.lineEdit_savings_amount.text()
                    )
                    savings_amount = int(
                        savings_amount_str.replace(",", "").replace(".", "")
                    )

                    match app_settings_dialog.comboBox_overflow_moneybox_modes.currentText():
                        case "collect":
                            mode = "collect"
                        case "add":
                            mode = "add_to_automated_savings_amount"
                        case "fill":
                            mode = "fill_up_limited_moneyboxes"
                        case _:
                            raise ValueError(
                                f"No supported {data['overflow_moneybox_automated_savings_mode']}"
                            )

                    async with PatchAppSettingsApiConsumer(
                        send_reports_via_email=app_settings_dialog.checkBox_send_reports_via_email.isChecked(),
                        user_email_address=app_settings_dialog.lineEdit_user_email_address.text(),
                        is_automated_saving_active=app_settings_dialog.checkBox_enable_automated_savings.isChecked(),
                        savings_amount=savings_amount,
                        overflow_moneybox_automated_savings_mode=mode,
                    ) as consumer:
                        if consumer.response.status_code == 200:
                            QMessageBox.information(
                                self,
                                "Updated AppSettings",
                                "Updated AppSettings successfully.",
                            )
                        else:
                            message_str = consumer.response.content.decode(
                                encoding="utf-8"
                            )
                            message = json.loads(message_str)["message"]
                            QMessageBox.warning(
                                self,
                                "Update AppSettings failed",
                                message,
                            )
            else:
                message_str = consumer.response.content.decode(encoding="utf-8")
                message = json.loads(message_str)["message"]
                QMessageBox.warning(
                    self,
                    "Transfer failed",
                    message,
                )

    async def load_moneybox_overview_widget(self, moneybox_id: int):
        async with GetMoneyboxApiConsumer(moneybox_id=moneybox_id) as consumer:
            if consumer.response.status_code == 200:
                data = consumer.response.json()
                moneybox_overview_widget = MoneyboxOverviewWidget(
                    parent_window=self,
                    moneybox_id=data["id"],
                    name_label=data["name"],
                    priority_label=str(data["priority"]),
                    savings_amount_label=(
                        f"{data['savings_amount'] / 100:.2f} €".replace(".", ",")
                    ),
                    savings_target_label=(
                        "No Limit"
                        if data["savings_target"] is None
                        else f"{data['savings_target'] / 100:.2f} €".replace(".", ",")
                    ),
                    balance_label=(f"{data['balance'] / 100:.2f} €".replace(".", ",")),
                )
                await self.switch_main_board_widget(child=moneybox_overview_widget)
            else:
                message_str = consumer.response.content.decode(encoding="utf-8")
                message = json.loads(message_str)["message"]
                QMessageBox.warning(
                    self,
                    "Transfer failed",
                    message,
                )

    async def load_moneyboxes_overview_widget(self):
        moneyboxes_overview_widget = MoneyboxesOverviewWidget(parent_window=self)
        await self.switch_main_board_widget(child=moneyboxes_overview_widget)

    async def switch_main_board_widget(self, child: QWidget):
        while self.main_board_layout.count() > 0:
            item = self.main_board_layout.takeAt(0)
            widget = item.widget()

            if widget is not None:
                widget.deleteLater()

        self.main_board_layout.addWidget(child)

        if hasattr(child, "load_api_content"):
            await child.load_api_content()

    @asyncClose
    async def closeEvent(self, event):
        pass
