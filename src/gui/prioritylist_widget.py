import asyncio
import json

from PySide6.QtWidgets import (QListWidgetItem, QMainWindow, QMessageBox,
                               QWidget)
from savings_manager_cli.api_consumers import (GetPriorityListApiConsumer,
                                               UpdatePriorityListApiConsumer)
from savings_manager_cli.custom_types import MoveDirection

from src.gui.ui.ui_prioritylist_widget import Ui_PriorityListWidget


class PrioritylistWidget(QWidget, Ui_PriorityListWidget):
    def __init__(
        self,
        parent_window: QMainWindow,
        parent: QWidget | None = None,
    ):
        self.parent_window = parent_window

        super().__init__(parent)
        self.setupUi(self)

        # connections
        self.pushButton_selected_up.clicked.connect(
            lambda: asyncio.ensure_future(self.move_item_up())
        )
        self.pushButton_selected_down.clicked.connect(
            lambda: asyncio.ensure_future(self.move_item_down())
        )

    async def move_item_up(self):
        current_row = self.listWidget_prioritylist.currentRow()

        if current_row > 0:  # Prüfen, ob es möglich ist, nach oben zu bewegen
            # Elementinformationen abrufen
            current_item = self.listWidget_prioritylist.takeItem(current_row)
            above_item = self.listWidget_prioritylist.takeItem(current_row - 1)

            # Elemente austauschen
            self.listWidget_prioritylist.insertItem(current_row - 1, current_item)
            self.listWidget_prioritylist.insertItem(current_row, above_item)

            # Auswahl auf das neue Element setzen
            self.listWidget_prioritylist.setCurrentRow(current_row - 1)

            async with UpdatePriorityListApiConsumer(
                moneybox_id=current_item.meta_data["moneybox_id"],
                move_direction=MoveDirection.UP,
                move_steps=1,
            ) as consumer:
                if consumer.response.status_code == 200:
                    pass  # move and save silently
                else:
                    message_str = consumer.response.content.decode(encoding="utf-8")
                    message = json.loads(message_str)["message"]
                    QMessageBox.warning(
                        self,
                        "Failed saving prioritylist",
                        message,
                    )

    async def move_item_down(self):
        current_row = self.listWidget_prioritylist.currentRow()
        total_rows = self.listWidget_prioritylist.count()

        if (
            current_row < total_rows - 1
        ):  # Prüfen, ob es möglich ist, nach unten zu bewegen
            # Aktuelles Element entfernen
            current_item = self.listWidget_prioritylist.takeItem(current_row)

            # Das Element unterhalb des aktuellen Elements einfügen
            self.listWidget_prioritylist.insertItem(current_row + 1, current_item)

            # Auswahl auf das neu verschobene Element setzen
            self.listWidget_prioritylist.setCurrentRow(current_row + 1)

            async with UpdatePriorityListApiConsumer(
                moneybox_id=current_item.meta_data["moneybox_id"],
                move_direction=MoveDirection.DOWN,
                move_steps=1,
            ) as consumer:
                if consumer.response.status_code == 200:
                    pass  # move and save silently
                else:
                    message_str = consumer.response.content.decode(encoding="utf-8")
                    message = json.loads(message_str)["message"]
                    QMessageBox.warning(
                        self,
                        "Failed saving prioritylist",
                        message,
                    )

    async def load_api_content(self):
        self.listWidget_prioritylist.clear()

        async with GetPriorityListApiConsumer() as consumer:
            if consumer.response.status_code == 200:
                sorted_by_priority_data = consumer.response.json()["priority_list"]

                for priority_data in sorted_by_priority_data:
                    item = QListWidgetItem(
                        f"{priority_data['name']} (ID: {priority_data['moneybox_id']})"
                    )
                    item.meta_data = priority_data
                    self.listWidget_prioritylist.addItem(item)

                self.listWidget_prioritylist.setCurrentRow(
                    len(sorted_by_priority_data) - 1
                )
            elif consumer.response.status_code == 204:
                # no data, do nothing
                return
            else:
                message_str = consumer.response.content.decode(encoding="utf-8")
                message = json.loads(message_str)["message"]
                QMessageBox.warning(
                    self,
                    "Failed loading prioritylist",
                    message,
                )
