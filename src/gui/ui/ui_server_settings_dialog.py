# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'server_settings_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QFrame,
                               QHBoxLayout, QLabel, QLineEdit, QPushButton,
                               QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)


class Ui_ServerSettingsDialog(object):
    def setupUi(self, ServerSettingsDialog):
        if not ServerSettingsDialog.objectName():
            ServerSettingsDialog.setObjectName("ServerSettingsDialog")
        ServerSettingsDialog.resize(280, 153)
        self.verticalLayout = QVBoxLayout(ServerSettingsDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_general_settings = QFrame(ServerSettingsDialog)
        self.frame_general_settings.setObjectName("frame_general_settings")
        self.frame_general_settings.setStyleSheet("border: 0px;")
        self.frame_general_settings.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_general_settings.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_general_settings)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_general_settings = QFormLayout()
        self.formLayout_general_settings.setObjectName("formLayout_general_settings")
        self.formLayout_general_settings.setContentsMargins(-1, -1, -1, 0)
        self.label = QLabel(self.frame_general_settings)
        self.label.setObjectName("label")

        self.formLayout_general_settings.setWidget(0, QFormLayout.LabelRole, self.label)

        self.lineEdit_host = QLineEdit(self.frame_general_settings)
        self.lineEdit_host.setObjectName("lineEdit_host")
        self.lineEdit_host.setStyleSheet("border: 1px solid black;")

        self.formLayout_general_settings.setWidget(
            0, QFormLayout.FieldRole, self.lineEdit_host
        )

        self.label_2 = QLabel(self.frame_general_settings)
        self.label_2.setObjectName("label_2")

        self.formLayout_general_settings.setWidget(
            1, QFormLayout.LabelRole, self.label_2
        )

        self.lineEdit_port = QLineEdit(self.frame_general_settings)
        self.lineEdit_port.setObjectName("lineEdit_port")
        self.lineEdit_port.setStyleSheet("border: 1px solid black;")

        self.formLayout_general_settings.setWidget(
            1, QFormLayout.FieldRole, self.lineEdit_port
        )

        self.verticalLayout_2.addLayout(self.formLayout_general_settings)

        self.verticalLayout.addWidget(self.frame_general_settings)

        self.frame_overflow_moneybox_settings = QFrame(ServerSettingsDialog)
        self.frame_overflow_moneybox_settings.setObjectName(
            "frame_overflow_moneybox_settings"
        )
        self.frame_overflow_moneybox_settings.setEnabled(False)
        self.frame_overflow_moneybox_settings.setStyleSheet("border: 0px;")
        self.frame_overflow_moneybox_settings.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_overflow_moneybox_settings.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_overflow_moneybox_settings)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.frame_overflow_moneybox_settings)

        self.verticalSpacer = QSpacerItem(
            0, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding
        )

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.horizontalSpacer_3 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.pushButton_apply = QPushButton(ServerSettingsDialog)
        self.pushButton_apply.setObjectName("pushButton_apply")

        self.horizontalLayout_2.addWidget(self.pushButton_apply)

        self.pushButton_cancel = QPushButton(ServerSettingsDialog)
        self.pushButton_cancel.setObjectName("pushButton_cancel")

        self.horizontalLayout_2.addWidget(self.pushButton_cancel)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(ServerSettingsDialog)

        # QMetaObject.connectSlotsByName(ServerSettingsDialog)

    # setupUi

    def retranslateUi(self, ServerSettingsDialog):
        ServerSettingsDialog.setWindowTitle(
            QCoreApplication.translate("ServerSettingsDialog", "Dialog", None)
        )
        self.label.setText(
            QCoreApplication.translate("ServerSettingsDialog", "Host", None)
        )
        self.label_2.setText(
            QCoreApplication.translate("ServerSettingsDialog", "Port: ", None)
        )
        self.pushButton_apply.setText(
            QCoreApplication.translate("ServerSettingsDialog", "&Apply", None)
        )
        self.pushButton_cancel.setText(
            QCoreApplication.translate("ServerSettingsDialog", "&Cancel", None)
        )

    # retranslateUi
