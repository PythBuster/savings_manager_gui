# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app_settings_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QFormLayout, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_AppSettingsDialog(object):
    def setupUi(self, AppSettingsDialog):
        if not AppSettingsDialog.objectName():
            AppSettingsDialog.setObjectName(u"AppSettingsDialog")
        AppSettingsDialog.resize(457, 234)
        self.verticalLayout = QVBoxLayout(AppSettingsDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_app_settings = QFrame(AppSettingsDialog)
        self.frame_app_settings.setObjectName(u"frame_app_settings")
        self.frame_app_settings.setStyleSheet(u"border: 0px;")
        self.frame_app_settings.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_app_settings.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_app_settings)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_general_settings = QFormLayout()
        self.formLayout_general_settings.setObjectName(u"formLayout_general_settings")
        self.formLayout_general_settings.setContentsMargins(-1, -1, -1, 0)
        self.lineEdit_savings_amount = QLineEdit(self.frame_app_settings)
        self.lineEdit_savings_amount.setObjectName(u"lineEdit_savings_amount")
        self.lineEdit_savings_amount.setStyleSheet(u"border: 1px solid black;")

        self.formLayout_general_settings.setWidget(0, QFormLayout.FieldRole, self.lineEdit_savings_amount)

        self.checkBox_enable_automated_savings = QCheckBox(self.frame_app_settings)
        self.checkBox_enable_automated_savings.setObjectName(u"checkBox_enable_automated_savings")

        self.formLayout_general_settings.setWidget(1, QFormLayout.LabelRole, self.checkBox_enable_automated_savings)

        self.checkBox_send_reports_via_email = QCheckBox(self.frame_app_settings)
        self.checkBox_send_reports_via_email.setObjectName(u"checkBox_send_reports_via_email")

        self.formLayout_general_settings.setWidget(2, QFormLayout.LabelRole, self.checkBox_send_reports_via_email)

        self.label_2 = QLabel(self.frame_app_settings)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFrameShape(QFrame.Shape.NoFrame)

        self.formLayout_general_settings.setWidget(4, QFormLayout.LabelRole, self.label_2)

        self.lineEdit_user_email_address = QLineEdit(self.frame_app_settings)
        self.lineEdit_user_email_address.setObjectName(u"lineEdit_user_email_address")
        self.lineEdit_user_email_address.setStyleSheet(u"border: 1px solid black;")

        self.formLayout_general_settings.setWidget(4, QFormLayout.FieldRole, self.lineEdit_user_email_address)

        self.label_3 = QLabel(self.frame_app_settings)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_general_settings.setWidget(5, QFormLayout.LabelRole, self.label_3)

        self.label = QLabel(self.frame_app_settings)
        self.label.setObjectName(u"label")

        self.formLayout_general_settings.setWidget(0, QFormLayout.LabelRole, self.label)

        self.comboBox_overflow_moneybox_modes = QComboBox(self.frame_app_settings)
        self.comboBox_overflow_moneybox_modes.addItem("")
        self.comboBox_overflow_moneybox_modes.addItem("")
        self.comboBox_overflow_moneybox_modes.addItem("")
        self.comboBox_overflow_moneybox_modes.setObjectName(u"comboBox_overflow_moneybox_modes")
        self.comboBox_overflow_moneybox_modes.setStyleSheet(u"border: 1px solid black;")

        self.formLayout_general_settings.setWidget(5, QFormLayout.FieldRole, self.comboBox_overflow_moneybox_modes)


        self.verticalLayout_2.addLayout(self.formLayout_general_settings)


        self.verticalLayout.addWidget(self.frame_app_settings)

        self.frame_overflow_moneybox_settings = QFrame(AppSettingsDialog)
        self.frame_overflow_moneybox_settings.setObjectName(u"frame_overflow_moneybox_settings")
        self.frame_overflow_moneybox_settings.setEnabled(False)
        self.frame_overflow_moneybox_settings.setStyleSheet(u"border: 0px;")
        self.frame_overflow_moneybox_settings.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_overflow_moneybox_settings.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_overflow_moneybox_settings)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.frame_overflow_moneybox_settings)

        self.verticalSpacer = QSpacerItem(0, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.pushButton_send_testemail = QPushButton(AppSettingsDialog)
        self.pushButton_send_testemail.setObjectName(u"pushButton_send_testemail")

        self.horizontalLayout_2.addWidget(self.pushButton_send_testemail)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.pushButton_apply = QPushButton(AppSettingsDialog)
        self.pushButton_apply.setObjectName(u"pushButton_apply")

        self.horizontalLayout_2.addWidget(self.pushButton_apply)

        self.pushButton_cancel = QPushButton(AppSettingsDialog)
        self.pushButton_cancel.setObjectName(u"pushButton_cancel")

        self.horizontalLayout_2.addWidget(self.pushButton_cancel)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        QWidget.setTabOrder(self.lineEdit_savings_amount, self.checkBox_enable_automated_savings)
        QWidget.setTabOrder(self.checkBox_enable_automated_savings, self.checkBox_send_reports_via_email)
        QWidget.setTabOrder(self.checkBox_send_reports_via_email, self.lineEdit_user_email_address)
        QWidget.setTabOrder(self.lineEdit_user_email_address, self.comboBox_overflow_moneybox_modes)
        QWidget.setTabOrder(self.comboBox_overflow_moneybox_modes, self.pushButton_send_testemail)
        QWidget.setTabOrder(self.pushButton_send_testemail, self.pushButton_apply)
        QWidget.setTabOrder(self.pushButton_apply, self.pushButton_cancel)

        self.retranslateUi(AppSettingsDialog)

        #QMetaObject.connectSlotsByName(AppSettingsDialog)
    # setupUi

    def retranslateUi(self, AppSettingsDialog):
        AppSettingsDialog.setWindowTitle(QCoreApplication.translate("AppSettingsDialog", u"Dialog", None))
        self.checkBox_enable_automated_savings.setText(QCoreApplication.translate("AppSettingsDialog", u"Enable Automated Savings", None))
        self.checkBox_send_reports_via_email.setText(QCoreApplication.translate("AppSettingsDialog", u"Send Reports via Email", None))
        self.label_2.setText(QCoreApplication.translate("AppSettingsDialog", u"User Email Address: ", None))
        self.label_3.setText(QCoreApplication.translate("AppSettingsDialog", u"Overflow Moneybox Mode: ", None))
        self.label.setText(QCoreApplication.translate("AppSettingsDialog", u"Savings Amounts: ", None))
        self.comboBox_overflow_moneybox_modes.setItemText(0, QCoreApplication.translate("AppSettingsDialog", u"collect", None))
        self.comboBox_overflow_moneybox_modes.setItemText(1, QCoreApplication.translate("AppSettingsDialog", u"add", None))
        self.comboBox_overflow_moneybox_modes.setItemText(2, QCoreApplication.translate("AppSettingsDialog", u"fill", None))

        self.pushButton_send_testemail.setText(QCoreApplication.translate("AppSettingsDialog", u"Save && send a test email", None))
        self.pushButton_apply.setText(QCoreApplication.translate("AppSettingsDialog", u"&Save", None))
        self.pushButton_cancel.setText(QCoreApplication.translate("AppSettingsDialog", u"&Cancel", None))
    # retranslateUi

