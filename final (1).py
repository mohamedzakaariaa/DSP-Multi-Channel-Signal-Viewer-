# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtPrintSupport
from PyQt5.QtGui import QScreen
from PyQt5.Qt import QFileInfo
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter, QPrintPreviewDialog
from PyQt5.QtWidgets import QFileDialog, QSlider
from scipy import signal
from fpdf import FPDF
from numpy.lib.function_base import average
from numpy.core.fromnumeric import mean, std
import matplotlib.pyplot as plt
import numpy as np
import sys
import pandas as pd
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import os
import pyqtgraph.exporters
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
import matplotlib
from pandas.core.base import SpecificationError
from pyqtgraph.widgets.ComboBox import ComboBox

matplotlib.use('Qt5Agg')

combotext1 = ""
combotext2 = ""
data1 = []
data2 = []
data3 = []


class pdf(FPDF):
    def __init__(self, figures, files, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.list_of_files = files
        self.list_of_figures = figures

    def generate_pdf(self):
        current_figure_number = 0
        current_signal_number = 1
        self.set_auto_page_break(auto=True, margin=15)
        statistics_data = self.making_statistics_data()
        for each_list in statistics_data:
            self.add_page()
            self.set_font("Arial", "B", size=30)
            self.cell(0, 25, txt=f"SIGNAL {current_signal_number}",
                      ln=1, align='C')
            self.set_font("Arial", size=20)
            self.cell(0, 15, txt=f"the maximum value is : {each_list[0]} mv",
                      ln=1)
            self.cell(0, 15, txt=f"the minimum value is : {each_list[1]} mv",
                      ln=1)
            self.cell(0, 15, txt=f"the mean_value is : {each_list[2]:.4f} mv",
                      ln=1)
            self.cell(0, 15, txt=f"the std value is : {each_list[3]:.4f} mv",
                      ln=1)
            self.cell(0, 15, txt=f"the signal duration is : {each_list[4]} sec",
                      ln=1)
            self.set_font("Arial", "B", size=20)
            self.cell(0, 15, txt=f"CURRENT STATUS OF THE SIGNAL",
                      ln=1, align="C")
            self.image(
                self.list_of_figures[current_figure_number], w=((self.w)*(2/3)))
            self.cell(0, 15, txt=f"SPECTROGRAM OF THE SIGNAL",
                      ln=1, align="C")
            self.image(
                self.list_of_figures[current_figure_number+1], w=((self.w)*(2/3)))
            current_figure_number += 2
            current_signal_number += 1
        self.output("Report.pdf")

    def making_statistics_data(self):
        statistics_list = []
        for element in range(0, len(self.list_of_files)):
            statistics_list.append(
                self.generate_statistics(self.list_of_files[element]))
        return statistics_list

    def generate_statistics(self, list_of_data):
        statistics = []
        time_of_each_value = 0.002
        minimum = min(list_of_data)
        maximum = max(list_of_data)
        the_mean = mean(list_of_data)
        standerd_diviation = std(list_of_data)
        duraion = len(list_of_data)*time_of_each_value
        statistics.append(maximum)
        statistics.append(minimum)
        statistics.append(the_mean)
        statistics.append(standerd_diviation)
        statistics.append(duraion)
        return statistics


class Ui_MainWindow(object):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.graph_figure_path = ""
        self.spectrogram_figure_path = "D:/programming/python/projects/dsp/spectrogram_figures"

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(753, 629)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.play_botton = QtWidgets.QPushButton(
            self.centralwidget)  # play button
        font = QtGui.QFont()
        font.setPointSize(12)
        self.play_botton.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pictures/play.jpeg"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play_botton.setIcon(icon)
        self.play_botton.setIconSize(QtCore.QSize(16, 20))
        self.play_botton.setCheckable(False)
        self.play_botton.setObjectName("play_botton")
        self.horizontalLayout.addWidget(self.play_botton)
        self.pause_botton = QtWidgets.QPushButton(
            self.centralwidget)  # pause button
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pause_botton.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("pictures/pause.jpeg"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pause_botton.setIcon(icon1)
        self.pause_botton.setIconSize(QtCore.QSize(40, 20))
        self.pause_botton.setObjectName("pause_botton")
        self.horizontalLayout.addWidget(self.pause_botton)
        self.zoom_in_botton = QtWidgets.QPushButton(
            self.centralwidget)  # zoom_in button
        font = QtGui.QFont()
        font.setPointSize(12)
        self.zoom_in_botton.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("pictures/zoom_in.jpeg"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoom_in_botton.setIcon(icon2)
        self.zoom_in_botton.setIconSize(QtCore.QSize(40, 20))
        self.zoom_in_botton.setObjectName("zoom_in_botton")
        self.horizontalLayout.addWidget(self.zoom_in_botton)
        self.zoom_out_botton = QtWidgets.QPushButton(
            self.centralwidget)  # zoom_out button
        font = QtGui.QFont()
        font.setPointSize(12)
        self.zoom_out_botton.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("pictures/zoom_out.jpeg"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoom_out_botton.setIcon(icon3)
        self.zoom_out_botton.setIconSize(QtCore.QSize(40, 20))
        self.zoom_out_botton.setObjectName("zoom_out_botton")
        self.horizontalLayout.addWidget(self.zoom_out_botton)
        self.show_botton = QtWidgets.QPushButton(
            self.centralwidget)  # show button
        self.show_botton.setBaseSize(QtCore.QSize(10, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.show_botton.setFont(font)
        self.show_botton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("pictures/showw.jpeg"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.show_botton.setIcon(icon4)
        self.show_botton.setIconSize(QtCore.QSize(0, 0))
        self.show_botton.setObjectName("show_botton")
        self.horizontalLayout.addWidget(self.show_botton)
        self.hide_botton = QtWidgets.QPushButton(
            self.centralwidget)  # hide button
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.hide_botton.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("pictures/hide.jpeg"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.hide_botton.setIcon(icon5)
        self.hide_botton.setObjectName("hide_botton")
        self.horizontalLayout.addWidget(self.hide_botton)
        self.spectrogram_botton = QtWidgets.QPushButton(
            self.centralwidget)  # specto button
        font = QtGui.QFont()
        font.setPointSize(14)
        self.spectrogram_botton.setFont(font)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("pictures/spectogram.jpeg"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.spectrogram_botton.setIcon(icon6)
        self.spectrogram_botton.setObjectName("spectrogram_botton")
        self.horizontalLayout.addWidget(self.spectrogram_botton)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.widget = QtWidgets.QWidget(self.splitter)
        self.widget.setObjectName("widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.main_graph = QtWidgets.QGraphicsView(self.widget)
        self.main_graph.setEnabled(True)
        self.main_graph.setMouseTracking(False)
        self.main_graph.setTabletTracking(False)
        self.main_graph.setAutoFillBackground(False)
        self.main_graph.setObjectName("main_graph")
        self.main_graph = PlotWidget(self.widget)
        self.main_graph.setStyleSheet("background: rgb(0,0,0)")
        self.horizontalLayout_5.addWidget(self.main_graph)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.EMG_label = QtWidgets.QLabel(self.widget)
        self.EMG_label.setAlignment(QtCore.Qt.AlignCenter)
        self.EMG_label.setObjectName("EMG_label")
        self.verticalLayout_3.addWidget(self.EMG_label)
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.ECG_label = QtWidgets.QLabel(self.widget)
        self.ECG_label.setAlignment(QtCore.Qt.AlignCenter)
        self.ECG_label.setObjectName("ECG_label")
        self.verticalLayout_3.addWidget(self.ECG_label)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.EOG_label = QtWidgets.QLabel(self.widget)
        self.EOG_label.setAlignment(QtCore.Qt.AlignCenter)
        self.EOG_label.setObjectName("EOG_label")
        self.verticalLayout_3.addWidget(self.EOG_label)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.signal_1_color_box = QtWidgets.QComboBox(self.widget)
        self.signal_1_color_box.setObjectName("signal_1_color_box")
        self.signal_1_color_box.addItem("")
        self.signal_1_color_box.addItem("")
        self.signal_1_color_box.addItem("")
        self.signal_1_color_box.addItem("")
        self.verticalLayout_6.addWidget(self.signal_1_color_box)
        self.dignal_2_color_box = QtWidgets.QComboBox(self.widget)
        self.dignal_2_color_box.setObjectName("dignal_2_color_box")
        self.dignal_2_color_box.addItem("")
        self.dignal_2_color_box.addItem("")
        self.dignal_2_color_box.addItem("")
        self.dignal_2_color_box.addItem("")
        self.verticalLayout_6.addWidget(self.dignal_2_color_box)
        self.signal_3_color_box = QtWidgets.QComboBox(self.widget)
        self.signal_3_color_box.setObjectName("signal_3_color_box")
        self.signal_3_color_box.addItem("")
        self.signal_3_color_box.addItem("")
        self.signal_3_color_box.addItem("")
        self.signal_3_color_box.addItem("")
        self.verticalLayout_6.addWidget(self.signal_3_color_box)
        self.horizontalLayout_5.addLayout(self.verticalLayout_6)
        self.verticalScrollBar = QtWidgets.QScrollBar(self.widget)
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.horizontalLayout_5.addWidget(self.verticalScrollBar)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalScrollBar = QtWidgets.QScrollBar(self.widget)
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.verticalLayout.addWidget(self.horizontalScrollBar)
        self.speed_slider = QtWidgets.QSlider(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.speed_slider.sizePolicy().hasHeightForWidth())
        self.speed_slider.setSizePolicy(sizePolicy)
        self.speed_slider.setOrientation(QtCore.Qt.Horizontal)
        self.speed_slider.setObjectName("speed_slider")
        self.speed_slider.setMinimum(50)
        self.speed_slider.setMaximum(800)
        self.speed_slider.setValue(400)
        self.speed_slider.setTickInterval(100)
        self.speed_slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.verticalLayout.addWidget(self.speed_slider)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.widget_2 = QtWidgets.QWidget(self.splitter)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.spectogram = QtWidgets.QVBoxLayout()
        self.spectogram.setObjectName("spectogram")
        self.horizontalLayout_2.addLayout(self.spectogram)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.color_paletta_box = QtWidgets.QComboBox(self.widget_2)
        self.color_paletta_box.setAutoFillBackground(False)
        self.color_paletta_box.setObjectName("color_paletta_box")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("pictures/palette.jpeg"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.color_paletta_box.addItem(icon7, "")
        self.color_paletta_box.addItem("")
        self.color_paletta_box.addItem("")
        self.color_paletta_box.addItem("")
        self.color_paletta_box.addItem("")
        self.color_paletta_box.addItem("")
        self.horizontalLayout_3.addWidget(self.color_paletta_box)
        self.contrast_max_slider = QtWidgets.QSlider(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.contrast_max_slider.sizePolicy().hasHeightForWidth())
        self.contrast_max_slider.setSizePolicy(sizePolicy)
        self.contrast_max_slider.setOrientation(QtCore.Qt.Vertical)
        self.contrast_max_slider.setInvertedAppearance(True)
        self.contrast_max_slider.setObjectName("contrast_max_slider")
        self.contrast_max_slider.setMinimum(-100)
        self.contrast_max_slider.setMaximum(-20)
        self.contrast_max_slider.setTickInterval(10)
        self.contrast_max_slider.setTickPosition(
            QSlider.TickPosition.TicksLeft)
        self.horizontalLayout_3.addWidget(self.contrast_max_slider)
        self.contrast_min_slider = QtWidgets.QSlider(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.contrast_min_slider.sizePolicy().hasHeightForWidth())
        self.contrast_min_slider.setSizePolicy(sizePolicy)
        self.contrast_min_slider.setOrientation(QtCore.Qt.Vertical)
        self.contrast_min_slider.setObjectName("contrast_min_slider")
        self.contrast_min_slider.setMinimum(-200)
        self.contrast_min_slider.setMaximum(-100)
        self.contrast_min_slider.setTickInterval(10)
        self.contrast_min_slider.setTickPosition(
            QSlider.TickPosition.TicksRight)
        self.horizontalLayout_3.addWidget(self.contrast_min_slider)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.signal_choice_box = QtWidgets.QComboBox(self.widget_2)
        self.signal_choice_box.setObjectName("signal_choice_box")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("pictures/change_signal.jpeg"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.signal_choice_box.addItem(icon8, "")
        self.signal_choice_box.addItem("")
        self.signal_choice_box.addItem("")
        self.signal_choice_box.addItem("")
        self.horizontalLayout_4.addWidget(self.signal_choice_box)
        self.submit_botton = QtWidgets.QPushButton(self.widget_2)
        self.submit_botton.setObjectName("submit_botton")
        self.horizontalLayout_4.addWidget(self.submit_botton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.verticalLayout_7.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 753, 21))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.Save_As_PDF_action = QtWidgets.QAction(MainWindow)
        self.Save_As_PDF_action.setObjectName("Save_As_PDF_action")
        self.actionChannel_2 = QtWidgets.QAction(MainWindow)
        self.actionChannel_2.setObjectName("actionChannel_2")
        self.actionChannel_1 = QtWidgets.QAction(MainWindow)
        self.actionChannel_1.setObjectName("actionChannel_1")
        self.actionChannel_3 = QtWidgets.QAction(MainWindow)
        self.actionChannel_3.setObjectName("actionChannel_3")
        self.actionChannel_4 = QtWidgets.QAction(MainWindow)
        self.actionChannel_4.setObjectName("actionChannel_4")
        self.Open_Signals_actoin = QtWidgets.QAction(MainWindow)
        self.Open_Signals_actoin.setObjectName("Open_Signals_actoin")
        self.menufile.addAction(self.Open_Signals_actoin)
        self.menufile.addSeparator()
        self.menufile.addAction(self.Save_As_PDF_action)
        self.menubar.addAction(self.menufile.menuAction())
        self.play_botton.clicked.connect(self.play)
        self.pause_botton.clicked.connect(self.pause_btn)
        self.zoom_in_botton.clicked.connect(self.zoom_in)
        self.zoom_out_botton.clicked.connect(self.zoom_out)
        self.speed_slider.sliderReleased.connect(self.Speed)
        self.spectrogram_botton.clicked.connect(self.ShowSpect)
        self.contrast_max_slider.valueChanged.connect(self.Spectrogram)
        self.contrast_min_slider.valueChanged.connect(self.Spectrogram)
        self.submit_botton.clicked.connect(self.Spectrogram)
        self.hide_botton.clicked.connect(self.hide)
        self.show_botton.clicked.connect(self.show)

        # self.Submit_2.clicked.connect(self.Spectrogram)

        self.widget_2.hide()
        self.EMG_label.hide()
        self.ECG_label.hide()
        self.EOG_label.hide()

        self.xmax_scale1 = 500
        self.xmin_scale1 = 0

        self.Open_Signals_actoin.triggered.connect(lambda: self.Open_Signal())
        self.Save_As_PDF_action.triggered.connect(self.Save_As_pdf)

        self.pen1 = pg.mkPen((255, 0, 0), width=3)
        self.pen2 = pg.mkPen((0, 255, 0), width=3)
        self.pen3 = pg.mkPen((0, 0, 255), width=3)

        self.x_range1 = self.main_graph.getViewBox().state['viewRange'][0]

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.play_botton.setText(_translate("MainWindow", "Play"))
        self.pause_botton.setText(_translate("MainWindow", "Pause"))
        self.zoom_in_botton.setText(_translate("MainWindow", "Zoom In"))
        self.zoom_out_botton.setText(_translate("MainWindow", "Zoom Out"))
        self.show_botton.setText(_translate("MainWindow", "Show"))
        self.hide_botton.setText(_translate("MainWindow", "Hide"))
        self.spectrogram_botton.setText(_translate("MainWindow", "SPECT"))
        self.EMG_label.setText(_translate("MainWindow", "EMG"))
        self.ECG_label.setText(_translate("MainWindow", "ECG"))
        self.EOG_label.setText(_translate("MainWindow", "EOG"))
        self.signal_1_color_box.setItemText(
            0, _translate("MainWindow", "signal 1 color"))
        self.signal_1_color_box.setItemText(1, _translate("MainWindow", "RED"))
        self.signal_1_color_box.setItemText(
            2, _translate("MainWindow", "BLUE"))
        self.signal_1_color_box.setItemText(
            3, _translate("MainWindow", "GREEN"))
        self.dignal_2_color_box.setItemText(
            0, _translate("MainWindow", "signal 2 color"))
        self.dignal_2_color_box.setItemText(1, _translate("MainWindow", "RED"))
        self.dignal_2_color_box.setItemText(
            2, _translate("MainWindow", "BLUE"))
        self.dignal_2_color_box.setItemText(
            3, _translate("MainWindow", "GREEN"))
        self.signal_3_color_box.setItemText(
            0, _translate("MainWindow", "signal 3 color"))
        self.signal_3_color_box.setItemText(1, _translate("MainWindow", "RED"))
        self.signal_3_color_box.setItemText(
            2, _translate("MainWindow", "BLUE"))
        self.signal_3_color_box.setItemText(
            3, _translate("MainWindow", "GREEN"))
        self.color_paletta_box.setItemText(
            0, _translate("MainWindow", " palettes"))
        self.color_paletta_box.setItemText(
            1, _translate("MainWindow", "Viridis"))
        self.color_paletta_box.setItemText(
            2, _translate("MainWindow", "Inferno"))
        self.color_paletta_box.setItemText(
            3, _translate("MainWindow", "Magma"))
        self.color_paletta_box.setItemText(
            4, _translate("MainWindow", "Cividis"))
        self.color_paletta_box.setItemText(
            5, _translate("MainWindow", "Plasma"))
        self.signal_choice_box.setItemText(
            0, _translate("MainWindow", "Choose Signal"))
        self.signal_choice_box.setItemText(1, _translate("MainWindow", "ECG"))
        self.signal_choice_box.setItemText(2, _translate("MainWindow", "EMG"))
        self.signal_choice_box.setItemText(3, _translate("MainWindow", "EOG"))
        self.submit_botton.setText(_translate("MainWindow", "Submit"))
        self.menufile.setTitle(_translate("MainWindow", "file"))
        self.Save_As_PDF_action.setText(
            _translate("MainWindow", "Save As PDF"))
        self.actionChannel_2.setText(_translate("MainWindow", "Channel 2"))
        self.actionChannel_1.setText(_translate("MainWindow", "Channel 1 "))
        self.actionChannel_3.setText(_translate("MainWindow", "Channel 2"))
        self.actionChannel_4.setText(_translate("MainWindow", "Channel 3"))
        self.Open_Signals_actoin.setText(
            _translate("MainWindow", "Open Signals"))

    def Open_Signal(self, flag):
        global F1, F2, F3, data1, data2, data3, time, selector
        selector = flag
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(
            None, "Open File", r"E:\CUFE\Signals", "Signals(*.csv)", options=options)
        data_set = pd.read_csv(fileName, header=1)
        data_set = data_set[1:].astype(float)
        File = data_set.iloc[:, 0]

        data = []
        time = []

        for i in range(1, (len(File)+1)):
            data.append(File[i])

        for i in range(0, (len(File))):
            time.append(i + self.x_range1[1])

        if flag == 1:
            F1 = File
            data1 = data
            if self.x_range1[0] == 0:
                self.main_graph.setXRange(self.xmin_scale1, self.xmax_scale1)
            else:
                self.main_graph.setXRange(self.x_range1[0], self.x_range1[1])
            self.x_range1 = self.main_graph.getViewBox(
            ).state['viewRange'][0]

        elif flag == 2:
            F2 = File
            data2 = data

            if self.x_range1[0] == 0:
                self.main_graph.setXRange(self.xmin_scale1, self.xmax_scale1)
            else:
                self.main_graph.setXRange(self.x_range1[0], self.x_range1[1])
            self.x_range1 = self.main_graph.getViewBox(
            ).state['viewRange'][0]

        else:
            F3 = File
            data3 = data

            if self.x_range1[0] == 0:
                self.main_graph.setXRange(self.xmin_scale1, self.xmax_scale1)
            else:
                self.main_graph.setXRange(self.x_range1[0], self.x_range1[1])
            self.x_range1 = self.main_graph.getViewBox(
            ).state['viewRange'][0]
        self.EMG_label.show()
        self.EOG_label.show()
        self.ECG_label.show()

    def update(self):
        # self.Change_signal1_color()
        # self.Change_signal2_color()
        # self.Change_signal3_color()
        # self.main_graph.plot(time, data1, pen=self.pen1)
        # self.main_graph.plot(time, data2, pen=self.pen2)
        # self.main_graph.plot(time, data3, pen=self.pen3)
        # self.main_graph.setXRange(self.x_range1[0], self.x_range1[1])
        # if self.x_range1[1] < time[len(time)-1]:
        #     self.x_range1[0] = self.x_range1[0]+50
        #     self.x_range1[1] = self.x_range1[1]+50
        self.Change_signal1_color()
        self.Change_signal2_color()
        self.Change_signal3_color()
        maxTime = 0
        if selector == 1:
            if time[len(time)-1] > maxTime:
                maxTime = time[len(time)-1]
            if self.x_range1[1] < time[len(time)-1]:
                self.x_range1[0] = self.x_range1[0]+50
                self.x_range1[1] = self.x_range1[1]+50
            self.main_graph.plot(time, data1, pen=self.pen2)
            self.main_graph.setXRange(self.x_range1[0], self.x_range1[1])

        if selector == 2:
            if time[len(time)-1] > maxTime:
                maxTime = time[len(time)-1]
            if self.x_range1[1] < time[len(time)-1]:
                self.x_range1[0] = self.x_range1[0]+50
                self.x_range1[1] = self.x_range1[1]+50
            self.main_graph.plot(time, data2, pen=self.pen3)
            self.main_graph.setXRange(self.x_range1[0], self.x_range1[1])

        if selector == 3:
            if time[len(time)-1] > maxTime:
                maxTime = time[len(time)-1]
            if self.x_range1[1] < time[len(time)-1]:
                self.x_range1[0] = self.x_range1[0]+50
                self.x_range1[1] = self.x_range1[1]+50
            # if self.x_range1[0] > time[len(time)-1]:
            #     maxTime = self.x_range1[0]
            self.main_graph.plot(time, data3, pen=self.pen1)
            self.main_graph.setXRange(self.x_range1[0], self.x_range1[1])

    def exporting_graph_figures(self):
        item = self.main_graph.plotItem
        exporter = pyqtgraph.exporters.ImageExporter(item)
        exporter.parameters()['width'] = 300
        exporter.export('graph_figures/graph_figure.png')
        self.graph_figure_path = "D:/programming/python/projects/dsp/graph_figures/graph_figure.png"

    def play(self):
        c = int(self.speed_slider.value())
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
        self.main_graph.setXRange(self.x_range1[0], self.x_range1[1])
        self.x_range1 = self.main_graph.getViewBox().state['viewRange'][0]

    def zoom_out(self):
        self.x_range1[1] = self.x_range1[1]*2
        self.x_range1[0] = self.x_range1[0]*2
        self.main_graph.setXRange(self.x_range1[0], self.x_range1[1])
        self.x_range1 = self.main_graph.getViewBox().state['viewRange'][0]

    def show(self):
        color1 = self.signal_1_color_box.currentText()
        if color1 == "RED":
            self.pen1 = pg.mkPen((255, 0, 0), width=3)
        elif color1 == "BLUE" or color1 == "signal 1 color":
            self.pen1 = pg.mkPen((0, 0, 255), width=3)
        elif color1 == "GREEN":
            self.pen1 = pg.mkPen((0, 255, 0), width=3)
        color2 = self.dignal_2_color_box.currentText()
        if color2 == "RED":
            self.pen2 = pg.mkPen((255, 0, 0), width=3)
        elif color2 == "BLUE":
            self.pen2 = pg.mkPen((0, 0, 255), width=3)
        elif color2 == "GREEN" or color2 == "signal 2 color":
            self.pen2 = pg.mkPen((0, 255, 0), width=3)

        color3 = self.signal_3_color_box.currentText()
        if color3 == "RED" or color3 == "signal 3 color":
            self.pen3 = pg.mkPen((255, 0, 0), width=3)
        elif color3 == "BLUE":
            self.pen3 = pg.mkPen((0, 0, 255), width=3)
        elif color3 == "GREEN":
            self.pen3 = pg.mkPen((0, 255, 0), width=3)

    def hide(self):
        self.pen1 = pg.mkPen((0, 0, 0), width=3)
        self.pen2 = pg.mkPen((0, 0, 0), width=3)
        self.pen3 = pg.mkPen((0, 0, 0), width=3)

    def Speed(self):
        global c
        c = int(self.speed_slider.value())
        self.play()

    def ShowSpect(self):
        self.widget_2.show()
        self.spec = MplCanvas(self, width=1, height=0.1)

    def Spectrogram(self):
        vmax = int(self.contrast_max_slider.value())
        vmin = int(self.contrast_min_slider.value())
        combotext1 = self.color_paletta_box.currentText()
        combotext2 = self.signal_choice_box.currentText()
        self.spec.deleteLater()
        if combotext2 == "ECG":
            self.spec = MplCanvas(self, width=1, height=0.1)
            if combotext1 == "Plasma":
                self.spec.axes.specgram(
                    F1, 900, cmap="plasma", vmax=vmax, vmin=vmin)
            elif combotext1 == "Viridis":
                self.spec.axes.specgram(
                    F1, 900, cmap="viridis", vmax=vmax, vmin=vmin)
            elif combotext1 == "Inferno":
                self.spec.axes.specgram(
                    F1, 900, cmap="inferno", vmax=vmax, vmin=vmin)
            elif combotext1 == "Magma":
                self.spec.axes.specgram(
                    F1, 900, cmap="magma", vmax=vmax, vmin=vmin)
            elif combotext1 == "Cividis":
                self.spec.axes.specgram(
                    F1, 900, cmap="cividis", vmax=vmax, vmin=vmin)
            self.spectogram.addWidget(self.spec)

        elif combotext2 == "EMG":
            self.spec = MplCanvas(self, width=1, height=0.1)
            if combotext1 == "Plasma":
                self.spec.axes.specgram(
                    F2, 900, cmap="plasma", vmax=vmax, vmin=vmin)
            elif combotext1 == "Viridis":
                self.spec.axes.specgram(
                    F2, 900, cmap="viridis", vmax=vmax, vmin=vmin)
            elif combotext1 == "Inferno":
                self.spec.axes.specgram(
                    F2, 900, cmap="inferno", vmax=vmax, vmin=vmin)
            elif combotext1 == "Magma":
                self.spec.axes.specgram(
                    F2, 900, cmap="magma", vmax=vmax, vmin=vmin)
            elif combotext1 == "Cividis":
                self.spec.axes.specgram(
                    F2, 900, cmap="cividis", vmax=vmax, vmin=vmin)
            self.spectogram.addWidget(self.spec)

        elif combotext2 == "EOG":
            self.spec = MplCanvas(self, width=1, height=0.1)
            if combotext1 == "Plasma":
                self.spec.axes.specgram(
                    F3, 900, cmap="plasma", vmax=vmax, vmin=vmin)
            elif combotext1 == "Viridis":
                self.spec.axes.specgram(
                    F3, 900, cmap="viridis", vmax=vmax, vmin=vmin)
            elif combotext1 == "Inferno":
                self.spec.axes.specgram(
                    F3, 900, cmap="inferno", vmax=vmax, vmin=vmin)
            elif combotext1 == "Magma":
                self.spec.axes.specgram(
                    F3, 900, cmap="magma", vmax=vmax, vmin=vmin)
            elif combotext1 == "Cividis":
                self.spec.axes.specgram(
                    F3, 900, cmap="cividis", vmax=vmax, vmin=vmin)
            self.spectogram.addWidget(self.spec)

    def Change_signal1_color(self):
        color1 = self.signal_1_color_box.currentText()
        if color1 == "RED":
            self.pen3 = pg.mkPen((255, 0, 0), width=3)
        elif color1 == "BLUE":
            self.pen3 = pg.mkPen((0, 0, 255), width=3)
        elif color1 == "GREEN":
            self.pen3 = pg.mkPen((0, 255, 0), width=3)

    def Change_signal2_color(self):
        color2 = self.dignal_2_color_box.currentText()
        if color2 == "RED":
            self.pen2 = pg.mkPen((255, 0, 0), width=3)
        elif color2 == "BLUE":
            self.pen2 = pg.mkPen((0, 0, 255), width=3)
        elif color2 == "GREEN":
            self.pen2 = pg.mkPen((0, 255, 0), width=3)

    def Change_signal3_color(self):
        color3 = self.signal_3_color_box.currentText()
        if color3 == "RED":
            self.pen1 = pg.mkPen((255, 0, 0), width=3)
        elif color3 == "BLUE":
            self.pen1 = pg.mkPen((0, 0, 255), width=3)
        elif color3 == "GREEN":
            self.pen1 = pg.mkPen((0, 255, 0), width=3)

    def Save_As_pdf(self):
        # [1,2,32,23,232,3,],[23,21,12,12,1,21],[2,3,23,23,23,23,23,23,256,56,5]
        list_of_data = [data1, data2, data3]
        # list_of_figures = ["D:/programming/python/projects/dsp/fileName.png", "D:/programming/python/projects/dsp/fileName.png", "D:/programming/python/projects/dsp/fileName.png",
        self.exporting_graph_figures()
        graph_path = self.graph_figure_path
        spectro_path = self.spectrogram_figure_path
        print(len(data1))
        # "D:/programming/python/projects/dsp/fileName.png", "D:/programming/python/projects/dsp/fileName.png", "D:/programming/python/projects/dsp/fileName.png"]
        list_of_figures = [graph_path, (spectro_path+"/EMG.jpeg"), graph_path,
                           (spectro_path+"/ECG.jpeg"), graph_path, (spectro_path+"/EOG.jpeg")]
        print("mahlasdkfjlsd")
        p = pdf(list_of_figures, list_of_data)
        print("mahlasdkfjlsd")
        p.generate_pdf()


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
