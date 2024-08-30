import asyncio

from PySide6.QtWidgets import QWidget, QMainWindow, QMessageBox, QPushButton, QLabel
from qasync import asyncClose, asyncSlot

from src.gui.moneyboxes_overview_widget import MoneyboxesOverviewWidget
from src.gui.ui.ui_main_window import Ui_MainWindow
from src.utils import get_app_data


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent: QWidget|None = None):
        super().__init__(parent)
        self.setupUi(self)

        app_data = get_app_data()
        app_title = f"Savings Manager GUI v{app_data['version']}"
        self.setWindowTitle(app_title)


        self.actionAbout_Qt.triggered.connect(
            lambda: QMessageBox.aboutQt(self, "About Qt")
        )
        self.actionAbout_Savings_Manager_GUI.triggered.connect(
            lambda: QMessageBox.about(self, f"About {app_title}", "...")
        )
        self.pushButton_MoneyboxesOverview.clicked.connect(
            lambda: asyncio.ensure_future(self.load_moneyboxes_overview_widget())
        )
        self.pushButton.clicked.connect(
            lambda: asyncio.ensure_future(self.switch_main_board_widget(QLabel))
        )
        self.pushButton_3.clicked.connect(
            lambda: asyncio.ensure_future(self.switch_main_board_widget(QPushButton))
        )

    @asyncSlot()
    async def on_enter_moneybox(self, moneybox_id: int):
        print("enter", moneybox_id)

    async def load_moneyboxes_overview_widget(self):
        moneyboxes_overview_widget = MoneyboxesOverviewWidget(parent_window=self)
        await self.switch_main_board_widget(moneyboxes_overview_widget)

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


