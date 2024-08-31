# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'moneybox_settings_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_MoneyboxSettingsDialog(object):
    def setupUi(self, MoneyboxSettingsDialog):
        if not MoneyboxSettingsDialog.objectName():
            MoneyboxSettingsDialog.setObjectName(u"MoneyboxSettingsDialog")
        MoneyboxSettingsDialog.resize(400, 300)
        self.verticalLayout = QVBoxLayout(MoneyboxSettingsDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(-1, -1, -1, 0)
        self.label = QLabel(MoneyboxSettingsDialog)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.lineEdit_name = QLineEdit(MoneyboxSettingsDialog)
        self.lineEdit_name.setObjectName(u"lineEdit_name")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_name)

        self.label_2 = QLabel(MoneyboxSettingsDialog)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.label_3 = QLabel(MoneyboxSettingsDialog)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.lineEdit_savings_amount = QLineEdit(MoneyboxSettingsDialog)
        self.lineEdit_savings_amount.setObjectName(u"lineEdit_savings_amount")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_savings_amount)

        self.lineEdit_savings_target = QLineEdit(MoneyboxSettingsDialog)
        self.lineEdit_savings_target.setObjectName(u"lineEdit_savings_target")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_savings_target)


        self.verticalLayout.addLayout(self.formLayout)

        self.verticalSpacer = QSpacerItem(0, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.pushButton_apply = QPushButton(MoneyboxSettingsDialog)
        self.pushButton_apply.setObjectName(u"pushButton_apply")

        self.horizontalLayout_2.addWidget(self.pushButton_apply)

        self.pushButton_cancel = QPushButton(MoneyboxSettingsDialog)
        self.pushButton_cancel.setObjectName(u"pushButton_cancel")

        self.horizontalLayout_2.addWidget(self.pushButton_cancel)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(MoneyboxSettingsDialog)

        QMetaObject.connectSlotsByName(MoneyboxSettingsDialog)
    # setupUi

    def retranslateUi(self, MoneyboxSettingsDialog):
        MoneyboxSettingsDialog.setWindowTitle(QCoreApplication.translate("MoneyboxSettingsDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("MoneyboxSettingsDialog", u"Name: ", None))
        self.label_2.setText(QCoreApplication.translate("MoneyboxSettingsDialog", u"Savings Amount: ", None))
        self.label_3.setText(QCoreApplication.translate("MoneyboxSettingsDialog", u"Savings Target: ", None))
        self.pushButton_apply.setText(QCoreApplication.translate("MoneyboxSettingsDialog", u"&Apply", None))
        self.pushButton_cancel.setText(QCoreApplication.translate("MoneyboxSettingsDialog", u"&Cancel", None))
    # retranslateUi

