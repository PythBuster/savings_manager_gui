from PySide6.QtWidgets import QWidget, QMainWindow, QMessageBox, QPushButton, QLabel
from qasync import asyncClose

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

        self.main_board_widgets = {
            MoneyboxesOverviewWidget: MoneyboxesOverviewWidget(),
            QPushButton: QPushButton("test"),
            QLabel: QLabel("test"),
        }

        for widget in self.main_board_widgets.values():
            self.main_layout.addWidget(widget)
            widget.setVisible(False)

        self.actionAbout_Qt.triggered.connect(
            lambda: QMessageBox.aboutQt(self, "About Qt")
        )
        self.actionAbout_Savings_Manager_GUI.triggered.connect(
            lambda: QMessageBox.about(self, f"About {app_title}", "...")
        )
        self.pushButton_MoneyboxesOverview.clicked.connect(
            lambda: self.switch_main_board_widget(MoneyboxesOverviewWidget)
        )
        self.pushButton.clicked.connect(
            lambda: self.switch_main_board_widget(QLabel)
        )
        self.pushButton_3.clicked.connect(
            lambda: self.switch_main_board_widget(QPushButton)
        )

    def switch_main_board_widget(self, child: QWidget):
        for widget in self.main_board_widgets.values():
            widget.setVisible(False)

        self.main_board_widgets[child].setVisible(True)

    @asyncClose
    async def closeEvent(self, event):
        pass


