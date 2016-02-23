# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SolMOKE_GUI.ui'
#
# Created: Tue Feb 23 09:06:26 2016
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1013, 723)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(220, 9, 791, 681))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.graphicsView = PlotWidget(self.verticalLayoutWidget)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.verticalLayout.addWidget(self.graphicsView)
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 50, 201, 137))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.stopBtn = QtGui.QPushButton(self.gridLayoutWidget)
        self.stopBtn.setObjectName(_fromUtf8("stopBtn"))
        self.gridLayout.addWidget(self.stopBtn, 6, 0, 1, 1)
        self.startBtn = QtGui.QPushButton(self.gridLayoutWidget)
        self.startBtn.setObjectName(_fromUtf8("startBtn"))
        self.gridLayout.addWidget(self.startBtn, 4, 0, 1, 1)
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.saveTimescanFileName = QtGui.QLineEdit(self.gridLayoutWidget)
        self.saveTimescanFileName.setObjectName(_fromUtf8("saveTimescanFileName"))
        self.gridLayout.addWidget(self.saveTimescanFileName, 1, 0, 1, 1)
        self.gridLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 190, 201, 137))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.stopHystBtn = QtGui.QPushButton(self.gridLayoutWidget_2)
        self.stopHystBtn.setObjectName(_fromUtf8("stopHystBtn"))
        self.gridLayout_2.addWidget(self.stopHystBtn, 7, 0, 1, 1)
        self.startHystBtn = QtGui.QPushButton(self.gridLayoutWidget_2)
        self.startHystBtn.setObjectName(_fromUtf8("startHystBtn"))
        self.gridLayout_2.addWidget(self.startHystBtn, 5, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.hystFileNameLabel = QtGui.QLabel(self.gridLayoutWidget_2)
        self.hystFileNameLabel.setMaximumSize(QtCore.QSize(77, 16777215))
        self.hystFileNameLabel.setObjectName(_fromUtf8("hystFileNameLabel"))
        self.horizontalLayout_2.addWidget(self.hystFileNameLabel)
        self.saveFileHystBtn = QtGui.QPushButton(self.gridLayoutWidget_2)
        self.saveFileHystBtn.setMinimumSize(QtCore.QSize(114, 31))
        self.saveFileHystBtn.setObjectName(_fromUtf8("saveFileHystBtn"))
        self.horizontalLayout_2.addWidget(self.saveFileHystBtn)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.workDirBtn = QtGui.QPushButton(self.centralwidget)
        self.workDirBtn.setGeometry(QtCore.QRect(60, 10, 95, 31))
        self.workDirBtn.setObjectName(_fromUtf8("workDirBtn"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.stopBtn.setText(_translate("MainWindow", "STOP", None))
        self.startBtn.setText(_translate("MainWindow", "START", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; text-decoration: underline; color:#00007f;\">Timescan</span></p></body></html>", None))
        self.stopHystBtn.setText(_translate("MainWindow", "STOP", None))
        self.startHystBtn.setText(_translate("MainWindow", "START", None))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; text-decoration: underline; color:#00007f;\">Hysteresis</span></p></body></html>", None))
        self.hystFileNameLabel.setText(_translate("MainWindow", "FileName", None))
        self.saveFileHystBtn.setText(_translate("MainWindow", "Save FileName", None))
        self.workDirBtn.setText(_translate("MainWindow", "WorkDir", None))

from pyqtgraph import PlotWidget
