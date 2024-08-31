# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'moneybox_overview_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect, QSize, Qt,
                            QTime, QUrl)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QGradient, QIcon, QImage,
                           QKeySequence, QLinearGradient, QPainter, QPalette,
                           QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea,
                               QApplication, QFormLayout, QFrame, QGridLayout,
                               QHBoxLayout, QHeaderView, QLabel, QPushButton,
                               QSizePolicy, QSpacerItem, QTableWidget,
                               QTableWidgetItem, QVBoxLayout, QWidget)


class Ui_MoneyboxOverviewWidget(object):
    def setupUi(self, MoneyboxOverviewWidget):
        if not MoneyboxOverviewWidget.objectName():
            MoneyboxOverviewWidget.setObjectName("MoneyboxOverviewWidget")
        MoneyboxOverviewWidget.resize(716, 398)
        self.horizontalLayout = QHBoxLayout(MoneyboxOverviewWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalSpacer = QSpacerItem(
            0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, 0, -1)
        self.label = QLabel(MoneyboxOverviewWidget)
        self.label.setObjectName("label")
        font = QFont()
        font.setBold(False)
        self.label.setFont(font)

        self.horizontalLayout_2.addWidget(self.label)

        self.label_name = QLabel(MoneyboxOverviewWidget)
        self.label_name.setObjectName("label_name")
        font1 = QFont()
        font1.setBold(True)
        self.label_name.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_name)

        self.horizontalSpacer_3 = QSpacerItem(
            0, 0, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(
            0, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed
        )

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.formLayout.setContentsMargins(-1, -1, -1, 0)
        self.label_id_title = QLabel(MoneyboxOverviewWidget)
        self.label_id_title.setObjectName("label_id_title")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_id_title)

        self.label_id = QLabel(MoneyboxOverviewWidget)
        self.label_id.setObjectName("label_id")
        self.label_id.setAlignment(
            Qt.AlignmentFlag.AlignRight
            | Qt.AlignmentFlag.AlignTrailing
            | Qt.AlignmentFlag.AlignVCenter
        )

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label_id)

        self.label_balance_title = QLabel(MoneyboxOverviewWidget)
        self.label_balance_title.setObjectName("label_balance_title")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_balance_title)

        self.label_balance = QLabel(MoneyboxOverviewWidget)
        self.label_balance.setObjectName("label_balance")
        self.label_balance.setAlignment(
            Qt.AlignmentFlag.AlignRight
            | Qt.AlignmentFlag.AlignTrailing
            | Qt.AlignmentFlag.AlignVCenter
        )

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.label_balance)

        self.label_savings_target_title = QLabel(MoneyboxOverviewWidget)
        self.label_savings_target_title.setObjectName("label_savings_target_title")

        self.formLayout.setWidget(
            3, QFormLayout.LabelRole, self.label_savings_target_title
        )

        self.label_savings_target = QLabel(MoneyboxOverviewWidget)
        self.label_savings_target.setObjectName("label_savings_target")
        self.label_savings_target.setAlignment(
            Qt.AlignmentFlag.AlignRight
            | Qt.AlignmentFlag.AlignTrailing
            | Qt.AlignmentFlag.AlignVCenter
        )

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.label_savings_target)

        self.label_savings_amount_title = QLabel(MoneyboxOverviewWidget)
        self.label_savings_amount_title.setObjectName("label_savings_amount_title")

        self.formLayout.setWidget(
            2, QFormLayout.LabelRole, self.label_savings_amount_title
        )

        self.label_savings_amount = QLabel(MoneyboxOverviewWidget)
        self.label_savings_amount.setObjectName("label_savings_amount")
        self.label_savings_amount.setAlignment(
            Qt.AlignmentFlag.AlignRight
            | Qt.AlignmentFlag.AlignTrailing
            | Qt.AlignmentFlag.AlignVCenter
        )

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.label_savings_amount)

        self.label_priority_title = QLabel(MoneyboxOverviewWidget)
        self.label_priority_title.setObjectName("label_priority_title")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_priority_title)

        self.label_priority = QLabel(MoneyboxOverviewWidget)
        self.label_priority.setObjectName("label_priority")
        self.label_priority.setAlignment(
            Qt.AlignmentFlag.AlignRight
            | Qt.AlignmentFlag.AlignTrailing
            | Qt.AlignmentFlag.AlignVCenter
        )

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.label_priority)

        self.horizontalLayout_4.addLayout(self.formLayout)

        self.horizontalSpacer_7 = QSpacerItem(
            46, 0, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)

        self.horizontalLayout_3.addLayout(self.horizontalLayout_4)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalSpacer_5 = QSpacerItem(
            10, 0, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum
        )

        self.gridLayout.addItem(self.horizontalSpacer_5, 0, 2, 1, 1)

        self.pushButton_sub_amount = QPushButton(MoneyboxOverviewWidget)
        self.pushButton_sub_amount.setObjectName("pushButton_sub_amount")

        self.gridLayout.addWidget(self.pushButton_sub_amount, 1, 1, 1, 1)

        self.pushButton_delete_moneybox = QPushButton(MoneyboxOverviewWidget)
        self.pushButton_delete_moneybox.setObjectName("pushButton_delete_moneybox")
        font2 = QFont()
        font2.setFamilies(["Ubuntu"])
        self.pushButton_delete_moneybox.setFont(font2)

        self.gridLayout.addWidget(self.pushButton_delete_moneybox, 1, 3, 1, 1)

        self.pushButton_settings = QPushButton(MoneyboxOverviewWidget)
        self.pushButton_settings.setObjectName("pushButton_settings")

        self.gridLayout.addWidget(self.pushButton_settings, 0, 3, 1, 1)

        self.pushButton_add_amount = QPushButton(MoneyboxOverviewWidget)
        self.pushButton_add_amount.setObjectName("pushButton_add_amount")

        self.gridLayout.addWidget(self.pushButton_add_amount, 0, 1, 1, 1)

        self.pushButton_transfer_amount = QPushButton(MoneyboxOverviewWidget)
        self.pushButton_transfer_amount.setObjectName("pushButton_transfer_amount")

        self.gridLayout.addWidget(self.pushButton_transfer_amount, 2, 1, 1, 1)

        self.horizontalLayout_3.addLayout(self.gridLayout)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.line = QFrame(MoneyboxOverviewWidget)
        self.line.setObjectName("line")
        self.line.setStyleSheet(
            "padding: 0px;\n"
            "margin: 0px;\n"
            "background-color: black;\n"
            "color: black;"
        )
        self.line.setLineWidth(1)
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.label_4 = QLabel(MoneyboxOverviewWidget)
        self.label_4.setObjectName("label_4")
        self.label_4.setFont(font1)

        self.verticalLayout.addWidget(self.label_4)

        self.tableWidget_transaction_logs = QTableWidget(MoneyboxOverviewWidget)
        if self.tableWidget_transaction_logs.columnCount() < 7:
            self.tableWidget_transaction_logs.setColumnCount(7)
        font3 = QFont()
        font3.setPointSize(11)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font3)
        self.tableWidget_transaction_logs.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font3)
        self.tableWidget_transaction_logs.setHorizontalHeaderItem(
            1, __qtablewidgetitem1
        )
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font3)
        self.tableWidget_transaction_logs.setHorizontalHeaderItem(
            2, __qtablewidgetitem2
        )
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font3)
        self.tableWidget_transaction_logs.setHorizontalHeaderItem(
            3, __qtablewidgetitem3
        )
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font3)
        self.tableWidget_transaction_logs.setHorizontalHeaderItem(
            4, __qtablewidgetitem4
        )
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font3)
        self.tableWidget_transaction_logs.setHorizontalHeaderItem(
            5, __qtablewidgetitem5
        )
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font3)
        self.tableWidget_transaction_logs.setHorizontalHeaderItem(
            6, __qtablewidgetitem6
        )
        self.tableWidget_transaction_logs.setObjectName("tableWidget_transaction_logs")
        self.tableWidget_transaction_logs.setFrameShape(QFrame.Shape.StyledPanel)
        self.tableWidget_transaction_logs.setSizeAdjustPolicy(
            QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored
        )
        self.tableWidget_transaction_logs.setEditTriggers(
            QAbstractItemView.EditTrigger.NoEditTriggers
        )
        self.tableWidget_transaction_logs.setSelectionMode(
            QAbstractItemView.SelectionMode.ExtendedSelection
        )
        self.tableWidget_transaction_logs.setSortingEnabled(False)

        self.verticalLayout.addWidget(self.tableWidget_transaction_logs)

        self.verticalLayout.setStretch(5, 1)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalSpacer_2 = QSpacerItem(
            0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.horizontalLayout.setStretch(1, 1)

        self.retranslateUi(MoneyboxOverviewWidget)

        # QMetaObject.connectSlotsByName(MoneyboxOverviewWidget)

    # setupUi

    def retranslateUi(self, MoneyboxOverviewWidget):
        MoneyboxOverviewWidget.setWindowTitle(
            QCoreApplication.translate("MoneyboxOverviewWidget", "Form", None)
        )
        self.label.setText(
            QCoreApplication.translate("MoneyboxOverviewWidget", "Moneybox:", None)
        )
        self.label_name.setText(
            QCoreApplication.translate(
                "MoneyboxOverviewWidget", "Overflow Moneybox", None
            )
        )
        self.label_id_title.setText(
            QCoreApplication.translate("MoneyboxOverviewWidget", "ID:", None)
        )
        self.label_id.setText(
            QCoreApplication.translate("MoneyboxOverviewWidget", "1", None)
        )
        self.label_balance_title.setText(
            QCoreApplication.translate("MoneyboxOverviewWidget", "Balance:", None)
        )
        self.label_balance.setText(
            QCoreApplication.translate("MoneyboxOverviewWidget", "123,45 \u20ac", None)
        )
        self.label_savings_target_title.setText(
            QCoreApplication.translate(
                "MoneyboxOverviewWidget", "Savings Target:", None
            )
        )
        self.label_savings_target.setText(
            QCoreApplication.translate("MoneyboxOverviewWidget", "1000,00 \u20ac", None)
        )
        self.label_savings_amount_title.setText(
            QCoreApplication.translate(
                "MoneyboxOverviewWidget", "Savings Amount:", None
            )
        )
        self.label_savings_amount.setText(
            QCoreApplication.translate("MoneyboxOverviewWidget", "150,00 \u20ac", None)
        )
        self.label_priority_title.setText(
            QCoreApplication.translate("MoneyboxOverviewWidget", "Priority:", None)
        )
        self.label_priority.setText(
            QCoreApplication.translate("MoneyboxOverviewWidget", "1", None)
        )
        self.pushButton_sub_amount.setText(
            QCoreApplication.translate("MoneyboxOverviewWidget", "&Sub Amount", None)
        )
        self.pushButton_delete_moneybox.setText(
            QCoreApplication.translate(
                "MoneyboxOverviewWidget", "&Delete Moneybox", None
            )
        )
        self.pushButton_settings.setText(
            QCoreApplication.translate("MoneyboxOverviewWidget", "Edit &Settings", None)
        )
        self.pushButton_add_amount.setText(
            QCoreApplication.translate("MoneyboxOverviewWidget", "&Add Amount", None)
        )
        self.pushButton_transfer_amount.setText(
            QCoreApplication.translate(
                "MoneyboxOverviewWidget", "&Transfer Amount", None
            )
        )
        self.label_4.setText(
            QCoreApplication.translate("MoneyboxOverviewWidget", "Transactions", None)
        )
        ___qtablewidgetitem = self.tableWidget_transaction_logs.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(
            QCoreApplication.translate("MoneyboxOverviewWidget", "date", None)
        )
        ___qtablewidgetitem1 = self.tableWidget_transaction_logs.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(
            QCoreApplication.translate("MoneyboxOverviewWidget", "trigger", None)
        )
        ___qtablewidgetitem2 = self.tableWidget_transaction_logs.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(
            QCoreApplication.translate("MoneyboxOverviewWidget", "type", None)
        )
        ___qtablewidgetitem3 = self.tableWidget_transaction_logs.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(
            QCoreApplication.translate("MoneyboxOverviewWidget", "counterparty", None)
        )
        ___qtablewidgetitem4 = self.tableWidget_transaction_logs.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(
            QCoreApplication.translate("MoneyboxOverviewWidget", "amount", None)
        )
        ___qtablewidgetitem5 = self.tableWidget_transaction_logs.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(
            QCoreApplication.translate("MoneyboxOverviewWidget", "balance", None)
        )
        ___qtablewidgetitem6 = self.tableWidget_transaction_logs.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(
            QCoreApplication.translate("MoneyboxOverviewWidget", "description", None)
        )

    # retranslateUi
