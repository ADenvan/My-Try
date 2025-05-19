# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'puls_5.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QProgressBar, QPushButton,
    QSizePolicy, QTableView, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(396, 529)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(10, 310, 371, 181))
        self.tableView.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tableView.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tableView.setShowGrid(False)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 130, 371, 131))
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.question_label = QLabel(self.widget)
        self.question_label.setObjectName(u"question_label")
        self.question_label.setMaximumSize(QSize(140, 100))
        font = QFont()
        font.setPointSize(30)
        self.question_label.setFont(font)

        self.horizontalLayout_2.addWidget(self.question_label)

        self.answer_input = QLineEdit(self.widget)
        self.answer_input.setObjectName(u"answer_input")
        self.answer_input.setEnabled(True)
        self.answer_input.setMaximumSize(QSize(70, 100))
        font1 = QFont()
        font1.setPointSize(30)
        self.answer_input.setFont(font1)

        self.horizontalLayout_2.addWidget(self.answer_input)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(10, 60, 371, 71))
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.time_label = QLabel(self.widget_2)
        self.time_label.setObjectName(u"time_label")
        self.time_label.setMaximumSize(QSize(30, 100))
        font2 = QFont()
        font2.setPointSize(18)
        self.time_label.setFont(font2)

        self.horizontalLayout.addWidget(self.time_label)

        self.progress_bar = QProgressBar(self.widget_2)
        self.progress_bar.setObjectName(u"progress_bar")
        self.progress_bar.setMaximumSize(QSize(200, 100))
        self.progress_bar.setValue(0)

        self.horizontalLayout.addWidget(self.progress_bar)

        self.start_btn = QPushButton(self.centralwidget)
        self.start_btn.setObjectName(u"start_btn")
        self.start_btn.setGeometry(QRect(120, 493, 171, 31))
        self.stats_label = QLabel(self.centralwidget)
        self.stats_label.setObjectName(u"stats_label")
        self.stats_label.setGeometry(QRect(18, 270, 361, 31))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.question_label.setText("")
        self.answer_input.setText("")
        self.time_label.setText("")
        self.start_btn.setText(QCoreApplication.translate("MainWindow", u"start ?", None))
        self.stats_label.setText("")
    # retranslateUi

