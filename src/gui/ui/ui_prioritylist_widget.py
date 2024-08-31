# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'prioritylist_widget.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QLabel,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_PriorityListWidget(object):
    def setupUi(self, PriorityListWidget):
        if not PriorityListWidget.objectName():
            PriorityListWidget.setObjectName(u"PriorityListWidget")
        PriorityListWidget.resize(428, 507)
        self.verticalLayout_2 = QVBoxLayout(PriorityListWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.label = QLabel(PriorityListWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setBold(True)
        self.label.setFont(font)

        self.verticalLayout_4.addWidget(self.label)

        self.listWidget_prioritylist = QListWidget(PriorityListWidget)
        self.listWidget_prioritylist.setObjectName(u"listWidget_prioritylist")
        font1 = QFont()
        font1.setPointSize(12)
        self.listWidget_prioritylist.setFont(font1)
        self.listWidget_prioritylist.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        self.verticalLayout_4.addWidget(self.listWidget_prioritylist)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.pushButton_selected_up = QPushButton(PriorityListWidget)
        self.pushButton_selected_up.setObjectName(u"pushButton_selected_up")
        self.pushButton_selected_up.setMinimumSize(QSize(50, 0))
        self.pushButton_selected_up.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_4.addWidget(self.pushButton_selected_up)

        self.pushButton_selected_down = QPushButton(PriorityListWidget)
        self.pushButton_selected_down.setObjectName(u"pushButton_selected_down")
        self.pushButton_selected_down.setMinimumSize(QSize(50, 0))
        self.pushButton_selected_down.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_4.addWidget(self.pushButton_selected_down)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)

        self.horizontalSpacer_2 = QSpacerItem(0, 0, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_2.setStretch(0, 1)

        self.retranslateUi(PriorityListWidget)

        #QMetaObject.connectSlotsByName(PriorityListWidget)
    # setupUi

    def retranslateUi(self, PriorityListWidget):
        PriorityListWidget.setWindowTitle(QCoreApplication.translate("PriorityListWidget", u"Form", None))
        self.label.setText(QCoreApplication.translate("PriorityListWidget", u"Prioritylist", None))
        self.pushButton_selected_up.setText(QCoreApplication.translate("PriorityListWidget", u"\u25b2", None))
        self.pushButton_selected_down.setText(QCoreApplication.translate("PriorityListWidget", u"\u25bc", None))
    # retranslateUi

