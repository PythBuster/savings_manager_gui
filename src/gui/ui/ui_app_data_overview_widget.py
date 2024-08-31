# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app_data_overview_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QLabel,
                               QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)


class Ui_AppDataOverviewWidget(object):
    def setupUi(self, AppDataOverviewWidget):
        if not AppDataOverviewWidget.objectName():
            AppDataOverviewWidget.setObjectName("AppDataOverviewWidget")
        AppDataOverviewWidget.resize(276, 194)
        self.verticalLayout = QVBoxLayout(AppDataOverviewWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QLabel(AppDataOverviewWidget)
        self.label.setObjectName("label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.label_savings_amount = QLabel(AppDataOverviewWidget)
        self.label_savings_amount.setObjectName("label_savings_amount")
        font = QFont()
        font.setBold(True)
        self.label_savings_amount.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label_savings_amount)

        self.label_3 = QLabel(AppDataOverviewWidget)
        self.label_3.setObjectName("label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.label_automated_savings_active_state = QLabel(AppDataOverviewWidget)
        self.label_automated_savings_active_state.setObjectName(
            "label_automated_savings_active_state"
        )
        self.label_automated_savings_active_state.setFont(font)

        self.formLayout.setWidget(
            1, QFormLayout.FieldRole, self.label_automated_savings_active_state
        )

        self.label_5 = QLabel(AppDataOverviewWidget)
        self.label_5.setObjectName("label_5")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_5)

        self.label_allocated_savings = QLabel(AppDataOverviewWidget)
        self.label_allocated_savings.setObjectName("label_allocated_savings")
        self.label_allocated_savings.setFont(font)

        self.formLayout.setWidget(
            2, QFormLayout.FieldRole, self.label_allocated_savings
        )

        self.label_7 = QLabel(AppDataOverviewWidget)
        self.label_7.setObjectName("label_7")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_7)

        self.label_not_allocated_savings = QLabel(AppDataOverviewWidget)
        self.label_not_allocated_savings.setObjectName("label_not_allocated_savings")
        self.label_not_allocated_savings.setFont(font)

        self.formLayout.setWidget(
            3, QFormLayout.FieldRole, self.label_not_allocated_savings
        )

        self.verticalLayout.addLayout(self.formLayout)

        self.line = QFrame(AppDataOverviewWidget)
        self.line.setObjectName("line")
        self.line.setStyleSheet(
            "padding: 0px;\n"
            "margin: 0px;\n"
            "background-color: black;\n"
            "color: black;"
        )
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.label_9 = QLabel(AppDataOverviewWidget)
        self.label_9.setObjectName("label_9")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        self.label_9.setFont(font1)
        self.label_9.setAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignVCenter
        )

        self.verticalLayout.addWidget(self.label_9)

        self.label_total_balance = QLabel(AppDataOverviewWidget)
        self.label_total_balance.setObjectName("label_total_balance")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.label_total_balance.setFont(font2)
        self.label_total_balance.setAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignVCenter
        )

        self.verticalLayout.addWidget(self.label_total_balance)

        self.verticalSpacer = QSpacerItem(
            0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding
        )

        self.verticalLayout.addItem(self.verticalSpacer)

        self.retranslateUi(AppDataOverviewWidget)

        # QMetaObject.connectSlotsByName(AppDataOverviewWidget)

    # setupUi

    def retranslateUi(self, AppDataOverviewWidget):
        AppDataOverviewWidget.setWindowTitle(
            QCoreApplication.translate("AppDataOverviewWidget", "Form", None)
        )
        self.label.setText(
            QCoreApplication.translate(
                "AppDataOverviewWidget", "App Savings Amount:", None
            )
        )
        self.label_savings_amount.setText(
            QCoreApplication.translate("AppDataOverviewWidget", "500,00 \u20ac", None)
        )
        self.label_3.setText(
            QCoreApplication.translate(
                "AppDataOverviewWidget", "Automated Savings:", None
            )
        )
        self.label_automated_savings_active_state.setText(
            QCoreApplication.translate("AppDataOverviewWidget", "Enabled", None)
        )
        self.label_5.setText(
            QCoreApplication.translate(
                "AppDataOverviewWidget", "Allocated Savings:", None
            )
        )
        self.label_allocated_savings.setText(
            QCoreApplication.translate("AppDataOverviewWidget", "400,00 \u20ac", None)
        )
        self.label_7.setText(
            QCoreApplication.translate(
                "AppDataOverviewWidget", "Not Allocated Savings:", None
            )
        )
        self.label_not_allocated_savings.setText(
            QCoreApplication.translate("AppDataOverviewWidget", "100,00 \u20ac", None)
        )
        self.label_9.setText(
            QCoreApplication.translate("AppDataOverviewWidget", "Total Balance:", None)
        )
        self.label_total_balance.setText(
            QCoreApplication.translate("AppDataOverviewWidget", "1234,00 \u20ac", None)
        )

    # retranslateUi
