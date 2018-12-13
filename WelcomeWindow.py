# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WelcomeWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from WorkWindow import Ui_WorkWindow


class Ui_MainWindow(object):

    def OpenWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_WorkWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(523, 350)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 501, 287))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.welcome_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.welcome_label.setGeometry(QtCore.QRect(130, 70, 231, 51))
        font = QtGui.QFont()
        font.setFamily("AngsanaUPC")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.welcome_label.setFont(font)
        self.welcome_label.setObjectName("welcome_label")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setGeometry(QtCore.QRect(60, 120, 401, 41))
        font = QtGui.QFont()
        font.setFamily("AngsanaUPC")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setGeometry(QtCore.QRect(190, 190, 121, 41))
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.OpenWindow)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 523, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.welcome_label.setText(_translate("MainWindow", "ДОБРО ПОЖАЛОВАТЬ В "))
        self.label.setText(_translate("MainWindow", "КОНСТРУКТОР ГРАФИКОВ"))
        self.pushButton.setText(_translate("MainWindow", "Начать!"))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    welcomeWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(welcomeWindow)
    welcomeWindow.show()
    sys.exit(app.exec())
