# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calc-untitled.ui_file'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QLineEdit, QMainWindow, QSizePolicy,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 500)
        MainWindow.setStyleSheet(u"QWidget {\n"
"                color: white;\n"
"                background-color: #121212;\n"
"                font-family: Rubik;\n"
"                font-size: 16pt;\n"
"                font-weight: 600;\n"
"                }")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        # self.textEdit.setLayoutDirection(Qt.LeftToRight)
        self.textEdit.setDocumentTitle(u"")
        self.textEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.textEdit)

        self.le_result = QLineEdit(self.centralwidget)
        self.le_result.setObjectName(u"le_result")
        self.le_result.setStyleSheet(u"font-size: 40pt;\n"
"border: none;\n"
"                            ")
        self.le_result.setMaxLength(30)
        self.le_result.setReadOnly(True)

        self.verticalLayout.addWidget(self.le_result)

        self.le_number = QLineEdit(self.centralwidget)
        self.le_number.setObjectName(u"le_number")
        self.le_number.setStyleSheet(u"font-size: 40pt;\n"
"border: none;\n"
"                            ")
        self.le_number.setMaxLength(30)
        self.le_number.setReadOnly(False)

        self.verticalLayout.addWidget(self.le_number)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Rubik'; font-size:16pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Text ?? </p></body></html>", None))
        self.le_result.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.le_number.setText(QCoreApplication.translate("MainWindow", u"", None))
    # retranslateUi

