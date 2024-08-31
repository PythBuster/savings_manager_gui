# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'moneybox_overview_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_MoneyboxOverviewWidget(object):
    def setupUi(self, MoneyboxOverviewWidget):
        if not MoneyboxOverviewWidget.objectName():
            MoneyboxOverviewWidget.setObjectName(u"MoneyboxOverviewWidget")
        MoneyboxOverviewWidget.resize(669, 303)
        self.horizontalLayout = QHBoxLayout(MoneyboxOverviewWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, 0, -1)
        self.label = QLabel(MoneyboxOverviewWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setBold(False)
        self.label.setFont(font)

        self.horizontalLayout_2.addWidget(self.label)

        self.label_name = QLabel(MoneyboxOverviewWidget)
        self.label_name.setObjectName(u"label_name")
        font1 = QFont()
        font1.setBold(True)
        self.label_name.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_name)

        self.horizontalSpacer_3 = QSpacerItem(0, 0, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(0, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(-1, -1, -1, 0)
        self.label_3 = QLabel(MoneyboxOverviewWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.label_id = QLabel(MoneyboxOverviewWidget)
        self.label_id.setObjectName(u"label_id")
        self.label_id.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label_id)

        self.label_5 = QLabel(MoneyboxOverviewWidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_5)

        self.label_balance = QLabel(MoneyboxOverviewWidget)
        self.label_balance.setObjectName(u"label_balance")
        self.label_balance.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.label_balance)

        self.label_7 = QLabel(MoneyboxOverviewWidget)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_7)

        self.label_savings_target = QLabel(MoneyboxOverviewWidget)
        self.label_savings_target.setObjectName(u"label_savings_target")
        self.label_savings_target.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.label_savings_target)

        self.label_9 = QLabel(MoneyboxOverviewWidget)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_9)

        self.label_savings_amount = QLabel(MoneyboxOverviewWidget)
        self.label_savings_amount.setObjectName(u"label_savings_amount")
        self.label_savings_amount.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.label_savings_amount)

        self.label_2 = QLabel(MoneyboxOverviewWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_2)

        self.label_priority = QLabel(MoneyboxOverviewWidget)
        self.label_priority.setObjectName(u"label_priority")
        self.label_priority.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.label_priority)


        self.horizontalLayout_4.addLayout(self.formLayout)

        self.horizontalSpacer_7 = QSpacerItem(46, 0, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_4)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_5 = QSpacerItem(10, 0, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 0, 2, 1, 1)

        self.pushButton_sub_amount = QPushButton(MoneyboxOverviewWidget)
        self.pushButton_sub_amount.setObjectName(u"pushButton_sub_amount")

        self.gridLayout.addWidget(self.pushButton_sub_amount, 1, 1, 1, 1)

        self.pushButton_delete_moneybox = QPushButton(MoneyboxOverviewWidget)
        self.pushButton_delete_moneybox.setObjectName(u"pushButton_delete_moneybox")
        font2 = QFont()
        font2.setFamilies([u"Ubuntu"])
        self.pushButton_delete_moneybox.setFont(font2)

        self.gridLayout.addWidget(self.pushButton_delete_moneybox, 1, 3, 1, 1)

        self.pushButton_settings = QPushButton(MoneyboxOverviewWidget)
        self.pushButton_settings.setObjectName(u"pushButton_settings")

        self.gridLayout.addWidget(self.pushButton_settings, 0, 3, 1, 1)

        self.pushButton_add_amount = QPushButton(MoneyboxOverviewWidget)
        self.pushButton_add_amount.setObjectName(u"pushButton_add_amount")

        self.gridLayout.addWidget(self.pushButton_add_amount, 0, 1, 1, 1)

        self.pushButton_transfer_amount = QPushButton(MoneyboxOverviewWidget)
        self.pushButton_transfer_amount.setObjectName(u"pushButton_transfer_amount")

        self.gridLayout.addWidget(self.pushButton_transfer_amount, 2, 1, 1, 1)


        self.horizontalLayout_3.addLayout(self.gridLayout)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.line = QFrame(MoneyboxOverviewWidget)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"padding: 0px;\n"
"margin: 0px;\n"
"background-color: black;\n"
"color: black;")
        self.line.setLineWidth(1)
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalSpacer_2 = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.horizontalLayout.setStretch(1, 1)

        self.retranslateUi(MoneyboxOverviewWidget)

        #QMetaObject.connectSlotsByName(MoneyboxOverviewWidget)
    # setupUi

    def retranslateUi(self, MoneyboxOverviewWidget):
        MoneyboxOverviewWidget.setWindowTitle(QCoreApplication.translate("MoneyboxOverviewWidget", u"Form", None))
        self.label.setText(QCoreApplication.translate("MoneyboxOverviewWidget", u"Moneybox:", None))
        self.label_name.setText(QCoreApplication.translate("MoneyboxOverviewWidget", u"Overflow Moneybox", None))
        self.label_3.setText(QCoreApplication.translate("MoneyboxOverviewWidget", u"ID:", None))
        self.label_id.setText(QCoreApplication.translate("MoneyboxOverviewWidget", u"1", None))
        self.label_5.setText(QCoreApplication.translate("MoneyboxOverviewWidget", u"Balance:", None))
        self.label_balance.setText(QCoreApplication.translate("MoneyboxOverviewWidget", u"123,45 \u20ac", None))
        self.label_7.setText(QCoreApplication.translate("MoneyboxOverviewWidget", u"Savings Target:", None))
        self.label_savings_target.setText(QCoreApplication.translate("MoneyboxOverviewWidget", u"1000,00 \u20ac", None))
        self.label_9.setText(QCoreApplication.translate("MoneyboxOverviewWidget", u"Savings Amount:", None))
        self.label_savings_amount.setText(QCoreApplication.translate("MoneyboxOverviewWidget", u"150,00 \u20ac", None))
        self.label_2.setText(QCoreApplication.translate("MoneyboxOverviewWidget", u"Priority:", None))
        self.label_priority.setText(QCoreApplication.translate("MoneyboxOverviewWidget", u"1", None))
        self.pushButton_sub_amount.setText(QCoreApplication.translate("MoneyboxOverviewWidget", u"&Sub Amount", None))
        self.pushButton_delete_moneybox.setText(QCoreApplication.translate("MoneyboxOverviewWidget", u"&Delete Moneybox", None))
        self.pushButton_settings.setText(QCoreApplication.translate("MoneyboxOverviewWidget", u"Edit &Settings", None))
        self.pushButton_add_amount.setText(QCoreApplication.translate("MoneyboxOverviewWidget", u"&Add Amount", None))
        self.pushButton_transfer_amount.setText(QCoreApplication.translate("MoneyboxOverviewWidget", u"&Transfer Amount", None))
    # retranslateUi

