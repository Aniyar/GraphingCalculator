# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'keyboard.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

value = ''


class Ui_MainWindow(object):

    def write(self, btn):
        self.leval += btn.text()
        self.lineEdit.setText(self.leval)

    def done(self):
        global value
        value = self.leval

    def backspace(self):
        self.leval = self.leval[:-1]
        self.lineEdit.setText(self.leval)

    def clear(self):
        self.leval = ''
        self.lineEdit.setText(self.leval)

    def setupUi(self, MainWindow):

        self.leval = ''
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(370, 354)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.Backspace = QtWidgets.QPushButton(self.centralwidget)
        self.Backspace.setGeometry(QtCore.QRect(10, 60, 51, 51))
        self.Backspace.setObjectName("Backspace")
        self.Backspace.clicked.connect(self.backspace)

        self.Clear_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Clear_btn.setGeometry(QtCore.QRect(60, 60, 51, 51))
        self.Clear_btn.setObjectName("Clear_btn")
        self.Clear_btn.clicked.connect(self.clear)

        self.plusminus_btn = QtWidgets.QPushButton(self.centralwidget)
        self.plusminus_btn.setGeometry(QtCore.QRect(160, 60, 51, 51))
        self.plusminus_btn.setObjectName("plusminus_btn")
        self.plusminus_btn.clicked.connect(self.write(self.plusminus_btn))

        self.root_btn = QtWidgets.QPushButton(self.centralwidget)
        self.root_btn.setGeometry(QtCore.QRect(210, 60, 51, 51))
        self.root_btn.setObjectName("root_btn")
        self.root_btn.clicked.connect(self.write(self.root_btn))

        self.seven_btn = QtWidgets.QPushButton(self.centralwidget)
        self.seven_btn.setGeometry(QtCore.QRect(10, 110, 51, 51))
        self.seven_btn.setObjectName("seven_btn")
        self.seven_btn.clicked.connect(self.write(self.seven_btn))

        self.eight_btn = QtWidgets.QPushButton(self.centralwidget)
        self.eight_btn.setGeometry(QtCore.QRect(60, 110, 51, 51))
        self.eight_btn.setObjectName("eight_btn")
        self.eight_btn.clicked.connect(self.write(self.eight_btn))

        self.nine_btn = QtWidgets.QPushButton(self.centralwidget)
        self.nine_btn.setGeometry(QtCore.QRect(110, 110, 51, 51))
        self.nine_btn.setObjectName("nine_btn")
        self.nine_btn.clicked.connect(self.write(self.nine_btn))

        self.division_btn = QtWidgets.QPushButton(self.centralwidget)
        self.division_btn.setGeometry(QtCore.QRect(160, 110, 51, 51))
        self.division_btn.setObjectName("division_btn")
        self.division_btn.clicked.connect(self.write(self.division_btn))

        self.degree_btn = QtWidgets.QPushButton(self.centralwidget)
        self.degree_btn.setGeometry(QtCore.QRect(210, 110, 51, 51))
        self.degree_btn.setObjectName("degree_btn")
        self.degree_btn.clicked.connect(self.write(self.degree_btn))

        self.four_btn = QtWidgets.QPushButton(self.centralwidget)
        self.four_btn.setGeometry(QtCore.QRect(10, 160, 51, 51))
        self.four_btn.setObjectName("four_btn")
        self.four_btn.clicked.connect(self.write(self.four_btn))

        self.five_btn = QtWidgets.QPushButton(self.centralwidget)
        self.five_btn.setGeometry(QtCore.QRect(60, 160, 51, 51))
        self.five_btn.setObjectName("five_btn")
        self.five_btn.clicked.connect(self.write(self.five_btn))

        self.six_btn = QtWidgets.QPushButton(self.centralwidget)
        self.six_btn.setGeometry(QtCore.QRect(110, 160, 51, 51))
        self.six_btn.setObjectName("six_btn")
        self.six_btn.clicked.connect(self.write(self.six_btn))

        self.multi_btn = QtWidgets.QPushButton(self.centralwidget)
        self.multi_btn.setGeometry(QtCore.QRect(160, 160, 51, 51))
        self.multi_btn.setObjectName("multi_btn")
        self.multi_btn.clicked.connect(self.write(self.multi_btn))

        self.opbracket_btn = QtWidgets.QPushButton(self.centralwidget)
        self.opbracket_btn.setGeometry(QtCore.QRect(210, 210, 51, 51))
        self.opbracket_btn.setObjectName("opbracket_btn")
        self.opbracket_btn.clicked.connect(self.write(self.opbracket_btn))

        self.one_btn = QtWidgets.QPushButton(self.centralwidget)
        self.one_btn.setGeometry(QtCore.QRect(10, 210, 51, 51))
        self.one_btn.setObjectName("one_btn")
        self.one_btn.clicked.connect(self.write(self.one_btn))

        self.two_btn = QtWidgets.QPushButton(self.centralwidget)
        self.two_btn.setGeometry(QtCore.QRect(60, 210, 51, 51))
        self.two_btn.setObjectName("two_btn")
        self.two_btn.clicked.connect(self.write(self.two_btn))

        self.three_btn = QtWidgets.QPushButton(self.centralwidget)
        self.three_btn.setGeometry(QtCore.QRect(110, 210, 51, 51))
        self.three_btn.setObjectName("three_btn")
        self.three_btn.clicked.connect(self.write(self.three_btn))

        self.minus_btn = QtWidgets.QPushButton(self.centralwidget)
        self.minus_btn.setGeometry(QtCore.QRect(160, 210, 51, 51))
        self.minus_btn.setObjectName("minus_btn")
        self.minus_btn.clicked.connect(self.write(self.minus_btn))

        self.clbracket_btn = QtWidgets.QPushButton(self.centralwidget)
        self.clbracket_btn.setGeometry(QtCore.QRect(210, 160, 51, 51))
        self.clbracket_btn.setObjectName("clbracket_btn")
        self.clbracket_btn.clicked.connect(self.write(self.clbracket_btn))

        self.zero_btn = QtWidgets.QPushButton(self.centralwidget)
        self.zero_btn.setGeometry(QtCore.QRect(10, 260, 101, 51))
        self.zero_btn.setObjectName("zero_btn")
        self.zero_btn.clicked.connect(self.write(self.zero_btn))

        self.sin_btn = QtWidgets.QPushButton(self.centralwidget)
        self.sin_btn.setGeometry(QtCore.QRect(260, 60, 51, 51))
        self.sin_btn.setObjectName("sin_btn")
        self.sin_btn.clicked.connect(self.write(self.sin_btn))

        self.dot_btn = QtWidgets.QPushButton(self.centralwidget)
        self.dot_btn.setGeometry(QtCore.QRect(110, 260, 51, 51))
        self.dot_btn.setObjectName("dot_btn")
        self.dot_btn.clicked.connect(self.write(self.dot_btn))

        self.plus_btn = QtWidgets.QPushButton(self.centralwidget)
        self.plus_btn.setGeometry(QtCore.QRect(160, 260, 51, 51))
        self.plus_btn.setObjectName("plus_btn")
        self.plus_btn.clicked.connect(self.write(self.plus_btn))

        self.done_btn = QtWidgets.QPushButton(self.centralwidget)
        self.done_btn.setGeometry(QtCore.QRect(210, 260, 151, 51))
        self.done_btn.setObjectName("done_btn")
        self.done_btn.clicked.connect(self.done)

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(40, 10, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")

        self.cos_btn = QtWidgets.QPushButton(self.centralwidget)
        self.cos_btn.setGeometry(QtCore.QRect(260, 110, 51, 51))
        self.cos_btn.setObjectName("cos_btn")
        self.cos_btn.clicked.connect(self.write(self.cos_btn))

        self.tan_btn = QtWidgets.QPushButton(self.centralwidget)
        self.tan_btn.setGeometry(QtCore.QRect(260, 160, 51, 51))
        self.tan_btn.setObjectName("tan_btn")
        self.tan_btn.clicked.connect(self.write(self.tan_btn))

        self.cot_btn = QtWidgets.QPushButton(self.centralwidget)
        self.cot_btn.setGeometry(QtCore.QRect(260, 210, 51, 51))
        self.cot_btn.setObjectName("cot_btn")
        self.cot_btn.clicked.connect(self.write(self.cot_btn))

        self.arcsin_btn = QtWidgets.QPushButton(self.centralwidget)
        self.arcsin_btn.setGeometry(QtCore.QRect(310, 60, 51, 51))
        self.arcsin_btn.setObjectName("arcsin_btn")
        self.arcsin_btn.clicked.connect(self.write(self.arcsin_btn))

        self.arccos_btn = QtWidgets.QPushButton(self.centralwidget)
        self.arccos_btn.setGeometry(QtCore.QRect(310, 110, 51, 51))
        self.arccos_btn.setObjectName("arccos_btn")
        self.arccos_btn.clicked.connect(self.write(self.arccos_btn))

        self.arctan_btn = QtWidgets.QPushButton(self.centralwidget)
        self.arctan_btn.setGeometry(QtCore.QRect(310, 160, 51, 51))
        self.arctan_btn.setObjectName("arctan_btn")
        self.arctan_btn.clicked.connect(self.write(self.arctan_btn))

        self.arccot_btn = QtWidgets.QPushButton(self.centralwidget)
        self.arccot_btn.setGeometry(QtCore.QRect(310, 210, 51, 51))
        self.arccot_btn.setObjectName("arccot_btn")
        self.arccot_btn.clicked.connect(self.write(self.arccot_btn))

        self.x_btn = QtWidgets.QPushButton(self.centralwidget)
        self.x_btn.setGeometry(QtCore.QRect(110, 60, 51, 51))
        self.x_btn.setObjectName("x_btn")
        self.x_btn.clicked.connect(self.write(self.x_btn))

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 370, 21))
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
        self.Backspace.setText(_translate("MainWindow", "<-"))
        self.Clear_btn.setText(_translate("MainWindow", "CE"))
        self.plusminus_btn.setText(_translate("MainWindow", "±"))
        self.root_btn.setText(_translate("MainWindow", "√"))
        self.seven_btn.setText(_translate("MainWindow", "7"))
        self.eight_btn.setText(_translate("MainWindow", "8"))
        self.nine_btn.setText(_translate("MainWindow", "9"))
        self.division_btn.setText(_translate("MainWindow", "/"))
        self.degree_btn.setText(_translate("MainWindow", "^"))
        self.four_btn.setText(_translate("MainWindow", "4"))
        self.five_btn.setText(_translate("MainWindow", "5"))
        self.six_btn.setText(_translate("MainWindow", "6"))
        self.multi_btn.setText(_translate("MainWindow", "*"))
        self.opbracket_btn.setText(_translate("MainWindow", "("))
        self.one_btn.setText(_translate("MainWindow", "1"))
        self.two_btn.setText(_translate("MainWindow", "2"))
        self.three_btn.setText(_translate("MainWindow", "3"))
        self.minus_btn.setText(_translate("MainWindow", "-"))
        self.clbracket_btn.setText(_translate("MainWindow", ")"))
        self.zero_btn.setText(_translate("MainWindow", "0"))
        self.sin_btn.setText(_translate("MainWindow", "sin"))
        self.dot_btn.setText(_translate("MainWindow", "."))
        self.plus_btn.setText(_translate("MainWindow", "+"))
        self.done_btn.setText(_translate("MainWindow", "Done"))
        self.cos_btn.setText(_translate("MainWindow", "cos"))
        self.tan_btn.setText(_translate("MainWindow", "tan"))
        self.cot_btn.setText(_translate("MainWindow", "cot"))
        self.arcsin_btn.setText(_translate("MainWindow", "arcsin"))
        self.arccos_btn.setText(_translate("MainWindow", "arccos"))
        self.arctan_btn.setText(_translate("MainWindow", "arctan"))
        self.arccot_btn.setText(_translate("MainWindow", "arccot"))
        self.x_btn.setText(_translate("MainWindow", "x"))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    kb = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(kb)
    kb.show()
    sys.exit(app.exec())