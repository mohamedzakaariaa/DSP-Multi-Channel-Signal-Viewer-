# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tam3.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtPrintSupport
from PyQt5.QtGui import QScreen
from PyQt5.Qt import QFileInfo
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter, QPrintPreviewDialog
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QFileDialog, QSlider
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
import sys
import pandas as pd
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import os
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
import matplotlib
from pyqtgraph.widgets.ComboBox import ComboBox
matplotlib.use('Qt5Agg')


combotext1 = ""
data1 = []
data2 = []
data3 = []


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(990, 1500)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 50, 920, 570))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.graphicsView = PlotWidget(self.verticalLayoutWidget)
        self.graphicsView.setStyleSheet("background: rgb(0,0,0)")
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(
            QtCore.QRect(120, 680, 671, 261))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 881, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_7 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_7.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Downloads/117098.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon)
        self.pushButton_7.setIconSize(QtCore.QSize(16, 20))
        self.pushButton_7.setCheckable(False)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout.addWidget(self.pushButton_7)
        self.pushButton_10 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_10.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../Downloads/download.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_10.setIcon(icon1)
        self.pushButton_10.setIconSize(QtCore.QSize(40, 20))
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout.addWidget(self.pushButton_10)
        self.pushButton_9 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_9.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(
            "../../Downloads/download (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_9.setIcon(icon2)
        self.pushButton_9.setIconSize(QtCore.QSize(40, 20))
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout.addWidget(self.pushButton_9)
        self.pushButton_8 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_8.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../Downloads/imagesss.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_8.setIcon(icon3)
        self.pushButton_8.setIconSize(QtCore.QSize(40, 20))
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout.addWidget(self.pushButton_8)
        self.pushButton_6 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_6.setBaseSize(QtCore.QSize(10, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6.setIconSize(QtCore.QSize(0, 0))
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout.addWidget(self.pushButton_6)
        self.pushButton_5 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)

        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(350, 650, 200, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider.setMinimum(50)
        self.horizontalSlider.setMaximum(800)
        self.horizontalSlider.setValue(400)
        self.horizontalSlider.setTickInterval(100)
        self.horizontalSlider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.verticalLayout.addWidget(self.horizontalSlider)    
        self.splitterLayout = QtWidgets.QSplitter(self.centralwidget)
        self.splitterLayout.addWidget(self.verticalLayoutWidget)
        self.splitterLayout.addWidget(self.verticalLayoutWidget_2)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(800, 750, 91, 22))
        self.comboBox.setObjectName("comboBox")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(
            "../color-palette-1594598-1348703.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon4, "Palettes")
        self.comboBox.addItem("Viridis")
        self.comboBox.addItem("Plasma")
        self.comboBox.addItem("Inferno")
        self.comboBox.addItem("Magma")
        self.comboBox.addItem("Cividis")

        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(800, 870, 91, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("Choose Signal")
        self.comboBox_2.addItem("ECG")
        self.comboBox_2.addItem("EMG")
        self.comboBox_2.addItem("EOG")

        self.Submit_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Submit_1.setGeometry(QtCore.QRect(900, 750, 75, 23))
        self.Submit_1.setObjectName("Submit_1")
        self.Submit_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Submit_2.setGeometry(QtCore.QRect(900, 870, 75, 23))
        self.Submit_2.setObjectName("Submit_2")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1121, 21))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        self.menuOpen_Signal = QtWidgets.QMenu(self.menufile)
        self.menuOpen_Signal.setObjectName("menuOpen_Signal")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)
        self.actionSave_As_PDF = QtWidgets.QAction(MainWindow)
        self.actionSave_As_PDF.setObjectName("actionSave_As_PDF")
        self.actionChannel_1 = QtWidgets.QAction(MainWindow)
        self.actionChannel_1.setObjectName("actionChannel_1")
        self.actionChannel_2 = QtWidgets.QAction(MainWindow)
        self.actionChannel_2.setObjectName("actionChannel_2")
        self.actionChannel_3 = QtWidgets.QAction(MainWindow)
        self.actionChannel_3.setObjectName("actionChannel_3")
        self.menuOpen_Signal.addAction(self.actionChannel_1)
        self.menuOpen_Signal.addSeparator()
        self.menuOpen_Signal.addAction(self.actionChannel_2)
        self.menuOpen_Signal.addSeparator()
        self.menuOpen_Signal.addAction(self.actionChannel_3)
        self.menufile.addAction(self.menuOpen_Signal.menuAction())
        self.menufile.addSeparator()
        self.menufile.addAction(self.actionSave_As_PDF)
        self.menubar.addAction(self.menufile.menuAction())

        self.pushButton_7.clicked.connect(self.play)
        self.pushButton_10.clicked.connect(self.pause_btn)
        self.pushButton_9.clicked.connect(self.zoom_in)
        self.pushButton_8.clicked.connect(self.zoom_out)
        self.pushButton.clicked.connect(self.ShowSpect)
        self.horizontalSlider.sliderReleased.connect(self.Speed)
        self.Submit_2.clicked.connect(self.Spectrogram)
        # self.pushButton_6.clicked.connect(self.show)
        # self.pushButton_5.clicked.connect(self.hide)
        # self.pushButton.clicked.connect(self.spectrogram)

        self.graphicsView.hide()
        self.horizontalSlider.hide()
        self.comboBox.hide()
        self.comboBox_2.hide()
        self.Submit_1.hide()
        self.Submit_2.hide()

        self.xmax_scale1 = 500
        self.xmin_scale1 = 0

        self.actionChannel_1.triggered.connect(lambda: self.Open_Signal(1))
        self.actionChannel_2.triggered.connect(lambda: self.Open_Signal(2))
        self.actionChannel_3.triggered.connect(lambda: self.Open_Signal(3))

        self.pen1 = pg.mkPen((255, 0, 0), width=3)
        self.pen2 = pg.mkPen((0, 255, 0), width=3)
        self.pen3 = pg.mkPen((0, 0, 255), width=3)

        self.x_range1 = self.graphicsView.getViewBox().state['viewRange'][0]

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_7.setText(_translate("MainWindow", "Play"))
        self.pushButton_10.setText(_translate("MainWindow", "Pause"))
        self.pushButton_9.setText(_translate("MainWindow", "Zoom In"))
        self.pushButton_8.setText(_translate("MainWindow", "Zoom Out"))
        self.pushButton_6.setText(_translate("MainWindow", "Show"))
        self.pushButton_5.setText(_translate("MainWindow", "Hide"))
        self.pushButton_4.setText(_translate("MainWindow", "Speed+"))
        self.pushButton_3.setText(_translate("MainWindow", "Speed-"))
        self.pushButton_2.setText(_translate("MainWindow", "S.Color"))
        self.pushButton.setText(_translate("MainWindow", "Spect."))
        self.menufile.setTitle(_translate("MainWindow", "file"))
        self.menuOpen_Signal.setTitle(_translate("MainWindow", "Open Signal"))
        self.actionSave_As_PDF.setText(_translate("MainWindow", "Save As PDF"))
        self.actionChannel_1.setText(_translate("MainWindow", "Channel 1 "))
        self.actionChannel_2.setText(_translate("MainWindow", "Channel 2"))
        self.actionChannel_3.setText(_translate("MainWindow", "Channel 3"))

    def Open_Signal(self, flag):
        global F1, F2, F3, data1, data2, data3, time, selector
        selector = flag
        # options = QFileDialog.Options()
        # fileName, _ = QFileDialog.getOpenFileName(
        #     None, "Open File", r"E:\CUFE\Signals", "Signals(data.csv)", options=options)
        data_set1 = pd.read_csv("signals\signal2.csv", header=1)
        data_set1 = data_set1[1:].astype(float)
        File1 = data_set1.iloc[:, 0]

        data_set2 = pd.read_csv("signals\ECG signal2.csv", header=1)
        data_set2 = data_set2[1:].astype(float)
        File2 = data_set2.iloc[:, 0]

        data_set3 = pd.read_csv("signals\emg2.csv", header=1)
        data_set3 = data_set3[1:].astype(float)
        File3 = data_set3.iloc[:, 0]

        F1 = File1
        F2 = File2
        F3 = File3

        time = []

        for i1 in range(1, (len(File1)+1)):
            data1.append(File1[i1])

        for i2 in range(1, (len(File2)+1)):
            data2.append(File2[i2])

        for i3 in range(1, (len(File3)+1)):
            data3.append(File3[i3])

        for j in range(0, (len(File1))):
            time.append(j)

        self.graphicsView.setXRange(self.xmin_scale1, self.xmax_scale1)
        self.x_range1 = self.graphicsView.getViewBox(
        ).state['viewRange'][0]
        self.graphicsView.show()
        self.horizontalSlider.show()

        # elif flag == 2:
        #     F2 = File
        #     data2 = data

        #     if self.x_range1[0] == 0:
        #         self.graphicsView.setXRange(self.xmin_scale1, self.xmax_scale1)
        #     else:
        #         self.graphicsView.setXRange(self.x_range1[0], self.x_range1[1])
        #     self.x_range1 = self.graphicsView.getViewBox(
        #     ).state['viewRange'][0]
        #     self.graphicsView.show()

        # else:
        #     F3 = File
        #     data3 = data

        #     if self.x_range1[0] == 0:
        #         self.graphicsView.setXRange(self.xmin_scale1, self.xmax_scale1)
        #     else:
        #         self.graphicsView.setXRange(self.x_range1[0], self.x_range1[1])
        #     self.x_range1 = self.graphicsView.getViewBox(
        #     ).state['viewRange'][0]
        #     self.graphicsView.show()

    def update(self):
        self.graphicsView.plot(time, data1, pen=self.pen1)
        self.graphicsView.plot(time, data2, pen=self.pen2)
        self.graphicsView.plot(time, data3, pen=self.pen3)
        self.graphicsView.setXRange(self.x_range1[0], self.x_range1[1])
        # if time[len(time)-1] > maxTime:
        #     maxTime = time[len(time)-1]
        if self.x_range1[1] < time[len(time)-1]:
            self.x_range1[0] = self.x_range1[0]+50
            self.x_range1[1] = self.x_range1[1]+50

        # if time[len(time)-1] > maxTime:
        #     maxTime = time[len(time)-1]
        # if self.x_range1[1] < time[len(time)-1]:
        #     self.x_range1[0] = self.x_range1[0]+10
        #     self.x_range1[1] = self.x_range1[1]+10

        # self.graphicsView.setXRange(self.x_range1[0], self.x_range1[1])

        # if time[len(time)-1] > maxTime:
        #     maxTime = time[len(time)-1]
        # if self.x_range1[1] < time[len(time)-1]:
        #     self.x_range1[0] = self.x_range1[0]+10
        #     self.x_range1[1] = self.x_range1[1]+10
        #  if self.x_range1[0] > time[len(time)-1]:
        #      maxTime = self.x_range1[0]
        # self.graphicsView.plot(time, data3, pen=self.pen3)
        # self.graphicsView.setXRange(self.x_range1[0], self.x_range1[1])

    def play(self):
        c = int(self.horizontalSlider.value())
        print(c)
        self.timer1 = pg.QtCore.QTimer()
        self.timer1.setInterval(10)
        self.timer1.timeout.connect(self.update)
        self.timer1.start(800-c)

    def pause_btn(self):
        self.timer1.stop()

    def zoom_in(self):
        self.x_range1[1] = self.x_range1[1]*0.5
        self.x_range1[0] = self.x_range1[0]*0.5
        self.graphicsView.setXRange(self.x_range1[0], self.x_range1[1])
        self.x_range1 = self.graphicsView.getViewBox().state['viewRange'][0]

    def zoom_out(self):
        self.x_range1[1] = self.x_range1[1]*2
        self.x_range1[0] = self.x_range1[0]*2
        self.graphicsView.setXRange(self.x_range1[0], self.x_range1[1])
        self.x_range1 = self.graphicsView.getViewBox().state['viewRange'][0]

    def Speed(self):
        global c
        c = int(self.horizontalSlider.value())
        self.play()

    def ShowSpect(self):
        self.spec = MplCanvas(self, width=1, height=0.1)
        self.comboBox.show()
        self.comboBox_2.show()
        self.Submit_1.show()
        self.Submit_2.show()

    # def Spectrogram(self):
    #     combotext1 = self.comboBox_2.currentText()
    #     self.spec.deleteLater()

    #     if combotext1 == "ECG":
    #         self.spec = MplCanvas(self, width=1, height=0.1)
    #         self.spec.axes.specgram(F1, 900, cmap="jet")
    #         self.verticalLayout_2.addWidget(self.spec)

    #     elif combotext1 == "EMG":
    #         self.spec = MplCanvas(self, width=1, height=0.1)
    #         self.spec.axes.specgram(F2, 900, cmap="jet")
    #         self.verticalLayout_2.addWidget(self.spec)

    #     elif combotext1 == "EOG":
    #         self.spec = MplCanvas(self, width=1, height=0.1)
    #         self.spec.axes.specgram(F3, 900, cmap="jet")
    #         self.verticalLayout_2.addWidget(self.spec)

    def Spectrogram(self):
        combotext2 = self.comboBox_2.currentText()
        combotext1 = self.comboBox.currentText()
        self.spec.deleteLater()
        if combotext2 == "ECG":
            self.spec = MplCanvas(self, width=1, height=0.1)
            if combotext1 == "Plasma":
                self.spec.axes.specgram(F1, 900, cmap="plasma")
            elif combotext1 == "Viridis":
                self.spec.axes.specgram(F1, 900, cmap="viridis")
            elif combotext1 == "Inferno":
                self.spec.axes.specgram(F1, 900, cmap="inferno")
            elif combotext1 == "Magma":
                self.spec.axes.specgram(F1, 900, cmap="magma")
            elif combotext1 == "Cividis":
                self.spec.axes.specgram(F1, 900, cmap="cividis")
            self.verticalLayout_2.addWidget(self.spec)

        if combotext2 == "EMG":
            self.spec = MplCanvas(self, width=1, height=0.1)
            if combotext1 == "plasma":
                self.spec.axes.specgram(F1, 900, cmap="plasma")
            elif combotext1 == "viridis":
                self.spec.axes.specgram(F1, 900, cmap="viridis")
            elif combotext1 == "inferno":
                self.spec.axes.specgram(F1, 900, cmap="inferno")
            elif combotext1 == "magma":
                self.spec.axes.specgram(F1, 900, cmap="magma")
            elif combotext1 == "cividis":
                self.spec.axes.specgram(F1, 900, cmap="cividis")
            self.verticalLayout_2.addWidget(self.spec)

        if combotext2 == "EOG":
            self.spec = MplCanvas(self, width=1, height=0.1)
            if combotext1 == "plasma":
                self.spec.axes.specgram(F1, 900, cmap="plasma")
            elif combotext1 == "viridis":
                self.spec.axes.specgram(F1, 900, cmap="viridis")
            elif combotext1 == "inferno":
                self.spec.axes.specgram(F1, 900, cmap="inferno")
            elif combotext1 == "magma":
                self.spec.axes.specgram(F1, 900, cmap="magma")
            elif combotext1 == "cividis":
                self.spec.axes.specgram(F1, 900, cmap="cividis")
            self.verticalLayout_2.addWidget(self.spec)


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
