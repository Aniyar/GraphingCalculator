# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WorkWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from numpy import arange
import pyqtgraph as pg
from math import sin, cos, tan
from keyboard import Ui_MainWindow
from ExceptionDialog import Ui_Dialog

class Ui_WorkWindow(object):

    def axes(self):  # рисует оси координат
        self.graphicsView.plot([i for i in arange(-self.k, self.k + 0.1, 0.1)],   # значение селф к = значение ползунка
                               [0 for x in arange(-self.k, self.k + 0.1, 0.1)],
                               pen='w')
        self.graphicsView.plot([0 for i in arange(-self.k, self.k + 0.1, 0.1)],
                               [x for x in arange(-self.k, self.k + 0.1, 0.1)],
                               pen='w')

    def color(self):  # ну вроде все понятно 
        color = QtWidgets.QColorDialog.getColor()
        if color.isValid():
            self.ColorButton.setStyleSheet(
                "background-color: {}".format(color.name())
            )
            self.clr = color.name()

    def run(self):   # запускается при нажатии кнопки Начертить. Чертит график функции из текстлайнэдита если это возможно.
                        # иначе открывает диалоговое окно 
        self.k = self.sl.value()
        self.graphicsView.setRange(yRange=[-self.k, self.k + 0.1])
        self.graphicsView.setRange(xRange=[-self.k, self.k + 0.1])
        self.axes()
        self.func = self.functionlineEdit.text()
        try:
            self.graphicsView.plot([i for i in arange(-self.k, self.k + 0.1, 0.1)],
                    [eval(self.func) for x in arange(-self.k, self.k + 0.1, 0.1)],
                    pen=self.clr)
        except Exception as e:  # ошибка срабатывает если эвал не сработал. А эвал не работает если функция неправильно записана
            self.ui = Ui_Dialog()  # открывает диалоговое окно. завершает ран
            self.ui.exec_()
            return
        word = '<span style=\" color: %s;\">%s</span>' % (self.clr, self.func)
        self.func_lst.append((self.func, self.clr))  # добавляет в текстбраузер и список функций введенную функцию 
        self.textBrowser.append(word)

    def scale_change(self):  # для повторной перерисовки графиков при изменении значения ползунка
        self.k = self.sl.value()
        self.graphicsView.setRange(yRange=[-self.k, self.k + 0.1])
        self.graphicsView.setRange(xRange=[-self.k, self.k + 0.1])
        self.axes()
        for i in self.func_lst:
            self.graphicsView.plot([j for j in arange(-self.k, self.k + 0.1, 0.1)],
                                   [eval(i[0]) for x in arange(-self.k, self.k + 0.1, 0.1)],
                                   pen=i[1])

    def clearall(self):  # при нажатии на кнопку "стереть все" стирает все
        self.graphicsView.clear()
        self.textBrowser.clear()
        self.func_lst = []

    def open_kb(self):   # открывает клавиатуру со специальными символами при нажатии кнопки "..."
        self.ui = Ui_MainWindow(self.kb_done)
        # self.ui.setupUi(self.window)
        self.ui.show()

    def kb_done(self):  # ставит значение из лайнэдита клавиатуры в лайнэдит главного окна при нажатии кнопки done
        self.functionlineEdit.setText(self.ui.get_value())

    def setupUi(self, WorkWindow):
        self.func_lst = []
        WorkWindow.setObjectName("WorkWindow")
        WorkWindow.resize(658, 595)

        self.centralwidget = QtWidgets.QWidget(WorkWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(510, 180, 141, 291))
        self.textBrowser.setObjectName("textBrowser")

        self.sl = QtWidgets.QSlider(self.centralwidget)
        self.sl.setGeometry(QtCore.QRect(510, 110, 121, 20))
        self.sl.setOrientation(QtCore.Qt.Horizontal)
        self.sl.setObjectName("sl")
        self.sl.setMinimum(1)
        self.sl.setMaximum(20)
        self.sl.setValue(1)
        self.sl.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.sl.setTickInterval(1)
        
        self.sl.valueChanged.connect(self.scale_change)

        self.DrawButton = QtWidgets.QPushButton(self.centralwidget)
        self.DrawButton.setGeometry(QtCore.QRect(460, 30, 121, 31))
        self.DrawButton.setObjectName("DrawButton")
        
        self.DrawButton.clicked.connect(self.run)

        self.FuctionsLabel = QtWidgets.QLabel(self.centralwidget)
        self.FuctionsLabel.setGeometry(QtCore.QRect(510, 140, 141, 31))

        font = QtGui.QFont()
        font.setPointSize(12)

        self.FuctionsLabel.setFont(font)
        self.FuctionsLabel.setObjectName("FuctionsLabel")
        self.functionlineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.functionlineEdit.setGeometry(QtCore.QRect(90, 40, 181, 21))
        self.functionlineEdit.setObjectName("functionlineEdit")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 40, 47, 13))

        font = QtGui.QFont()
        font.setPointSize(10)

        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.KeyboardButton = QtWidgets.QPushButton(self.centralwidget)
        self.KeyboardButton.setGeometry(QtCore.QRect(280, 40, 31, 21))
        self.KeyboardButton.setObjectName("KeyboardButton")
        
        self.KeyboardButton.clicked.connect(self.open_kb)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 239, 27))

        font = QtGui.QFont()
        font.setFamily("Angsana New")
        font.setPointSize(14)

        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(510, 90, 241, 20))

        font = QtGui.QFont()
        font.setFamily("AngsanaUPC")
        font.setPointSize(12)

        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.ColorButton = QtWidgets.QPushButton(self.centralwidget)
        self.ColorButton.setGeometry(QtCore.QRect(330, 30, 121, 31))
        self.ColorButton.setObjectName("ColorButton")
        
        self.ColorButton.clicked.connect(self.color)

        self.graphicsView = pg.PlotWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 90, 491, 461))
        self.graphicsView.setObjectName("graphicsView")

        self.ClearButton = QtWidgets.QPushButton(self.centralwidget)
        self.ClearButton.setGeometry(QtCore.QRect(510, 500, 121, 31))
        self.ClearButton.setObjectName("ClearButton")
        
        self.ClearButton.clicked.connect(self.clearall)

        WorkWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(WorkWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 658, 21))
        self.menubar.setObjectName("menubar")
        WorkWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(WorkWindow)
        self.statusbar.setObjectName("statusbar")
        WorkWindow.setStatusBar(self.statusbar)

        self.retranslateUi(WorkWindow)
        QtCore.QMetaObject.connectSlotsByName(WorkWindow)

    def retranslateUi(self, WorkWindow):
        _translate = QtCore.QCoreApplication.translate
        WorkWindow.setWindowTitle(_translate("WorkWindow", "MainWindow"))
        self.DrawButton.setText(_translate("WorkWindow", "Нарисовать график!"))
        self.FuctionsLabel.setText(_translate("WorkWindow", "Функции:"))
        self.label_2.setText(_translate("WorkWindow", "f(x) = "))
        self.KeyboardButton.setText(_translate("WorkWindow", "..."))
        self.label.setText(_translate("WorkWindow", "Введите значение функции:"))
        self.label_3.setText(_translate("WorkWindow", "Укажите масштаб:"))
        self.ColorButton.setText(_translate("WorkWindow", "Выберите цвет"))
        self.ClearButton.setText(_translate("WorkWindow", "Стереть все"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    workWindow = QtWidgets.QMainWindow()
    ui = Ui_WorkWindow()
    ui.setupUi(workWindow)
    workWindow.show()
    sys.exit(app.exec())
