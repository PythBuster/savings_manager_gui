import asyncio

from PySide6.QtWidgets import QWidget, QMainWindow, QMessageBox, QPushButton, QLabel
from qasync import asyncClose, asyncSlot
from savings_manager_cli.api_consumers import GetMoneyboxApiConsumer

from src.gui.moneybox_overview_widget import MoneyboxOverviewWidget
from src.gui.moneyboxes_overview_widget import MoneyboxesOverviewWidget
from src.gui.prioritylist_widget import PrioritylistWidget
from src.gui.ui.ui_main_window import Ui_MainWindow
from src.utils import get_app_data


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent: QWidget|None = None):
        super().__init__(parent)
        self.setupUi(self)

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

        # connection - navigation buttons
        self.pushButton_MoneyboxesOverview.clicked.connect(
            lambda: asyncio.ensure_future(self.load_moneyboxes_overview_widget())
        )
        self.pushButton_PrioritylistWidget.clicked.connect(
            lambda: asyncio.ensure_future(self.load_prioritylist_widget())
        )
        self.pushButton_AppSettingsWidget.clicked.connect(
            lambda: asyncio.ensure_future(self.switch_main_board_widget(QPushButton))
        )

    @asyncSlot()
    async def on_enter_moneybox(self, moneybox_id: int):
        await self.load_moneybox_overview_widget(moneybox_id=moneybox_id)

    async def load_prioritylist_widget(self):
        prioritylist_widget = PrioritylistWidget(parent_window=self)
        await self.switch_main_board_widget(child=prioritylist_widget)

    async def load_moneybox_overview_widget(self, moneybox_id:int ):
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
                    balance_label=(
                        f"{data['balance'] / 100:.2f} €".replace(".", ",")
                    ),
                )
                await self.switch_main_board_widget(child=moneybox_overview_widget)
            else:
                # TODO: raise / inform user about error
                return

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


