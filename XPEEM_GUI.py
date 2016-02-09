# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'XPEEM_GUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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
        MainWindow.resize(1337, 818)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.French, QtCore.QLocale.France))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(450, 10, 851, 761))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.imageView = ImageView(self.verticalLayoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageView.sizePolicy().hasHeightForWidth())
        self.imageView.setSizePolicy(sizePolicy)
        self.imageView.setObjectName(_fromUtf8("imageView"))
        self.verticalLayout_2.addWidget(self.imageView)
        self.verticalLayoutWidget_3 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 390, 431, 381))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.plotView = PlotWidget(self.verticalLayoutWidget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plotView.sizePolicy().hasHeightForWidth())
        self.plotView.setSizePolicy(sizePolicy)
        self.plotView.setObjectName(_fromUtf8("plotView"))
        self.verticalLayout_3.addWidget(self.plotView)
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 11, 429, 371))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pickROIBtn = QtGui.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Optima"))
        font.setPointSize(14)
        self.pickROIBtn.setFont(font)
        self.pickROIBtn.setAutoFillBackground(False)
        self.pickROIBtn.setFlat(False)
        self.pickROIBtn.setObjectName(_fromUtf8("pickROIBtn"))
        self.gridLayout.addWidget(self.pickROIBtn, 0, 1, 1, 1)
        self.calcSingleSpectrumBtn = QtGui.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Optima"))
        font.setPointSize(14)
        self.calcSingleSpectrumBtn.setFont(font)
        self.calcSingleSpectrumBtn.setObjectName(_fromUtf8("calcSingleSpectrumBtn"))
        self.gridLayout.addWidget(self.calcSingleSpectrumBtn, 1, 1, 1, 1)
        self.load2nrjBtn = QtGui.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Optima"))
        font.setPointSize(14)
        self.load2nrjBtn.setFont(font)
        self.load2nrjBtn.setCheckable(False)
        self.load2nrjBtn.setObjectName(_fromUtf8("load2nrjBtn"))
        self.gridLayout.addWidget(self.load2nrjBtn, 5, 0, 1, 1)
        self.load2polBtn = QtGui.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Optima"))
        font.setPointSize(14)
        self.load2polBtn.setFont(font)
        self.load2polBtn.setCheckable(False)
        self.load2polBtn.setObjectName(_fromUtf8("load2polBtn"))
        self.gridLayout.addWidget(self.load2polBtn, 4, 0, 1, 1)
        self.load2XASBtn = QtGui.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Optima"))
        font.setPointSize(14)
        self.load2XASBtn.setFont(font)
        self.load2XASBtn.setObjectName(_fromUtf8("load2XASBtn"))
        self.gridLayout.addWidget(self.load2XASBtn, 2, 0, 1, 1)
        self.loadXASBtn = QtGui.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Optima"))
        font.setPointSize(14)
        self.loadXASBtn.setFont(font)
        self.loadXASBtn.setObjectName(_fromUtf8("loadXASBtn"))
        self.gridLayout.addWidget(self.loadXASBtn, 1, 0, 1, 1)
        self.chooseWorkDirectoryBtn = QtGui.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Optima"))
        font.setPointSize(14)
        self.chooseWorkDirectoryBtn.setFont(font)
        self.chooseWorkDirectoryBtn.setObjectName(_fromUtf8("chooseWorkDirectoryBtn"))
        self.gridLayout.addWidget(self.chooseWorkDirectoryBtn, 0, 0, 1, 1)
        self.calcDiffSpectraBtn = QtGui.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Optima"))
        font.setPointSize(14)
        self.calcDiffSpectraBtn.setFont(font)
        self.calcDiffSpectraBtn.setObjectName(_fromUtf8("calcDiffSpectraBtn"))
        self.gridLayout.addWidget(self.calcDiffSpectraBtn, 2, 1, 1, 1)
        self.loadNormFileBtn = QtGui.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Optima"))
        font.setPointSize(14)
        self.loadNormFileBtn.setFont(font)
        self.loadNormFileBtn.setObjectName(_fromUtf8("loadNormFileBtn"))
        self.gridLayout.addWidget(self.loadNormFileBtn, 3, 0, 1, 1)
        self.calcDiffImagesBtn = QtGui.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Optima"))
        font.setPointSize(14)
        self.calcDiffImagesBtn.setFont(font)
        self.calcDiffImagesBtn.setCheckable(False)
        self.calcDiffImagesBtn.setObjectName(_fromUtf8("calcDiffImagesBtn"))
        self.gridLayout.addWidget(self.calcDiffImagesBtn, 3, 1, 1, 1)
        self.plotDriftBtn = QtGui.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Optima"))
        font.setPointSize(14)
        self.plotDriftBtn.setFont(font)
        self.plotDriftBtn.setCheckable(False)
        self.plotDriftBtn.setObjectName(_fromUtf8("plotDriftBtn"))
        self.gridLayout.addWidget(self.plotDriftBtn, 4, 1, 1, 1)
        self.clearBtn = QtGui.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Optima"))
        font.setPointSize(14)
        self.clearBtn.setFont(font)
        self.clearBtn.setCheckable(False)
        self.clearBtn.setObjectName(_fromUtf8("clearBtn"))
        self.gridLayout.addWidget(self.clearBtn, 5, 1, 1, 1)
        self.switchStackShow1Btn = QtGui.QRadioButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Optima"))
        font.setPointSize(14)
        self.switchStackShow1Btn.setFont(font)
        self.switchStackShow1Btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.switchStackShow1Btn.setAutoFillBackground(True)
        self.switchStackShow1Btn.setObjectName(_fromUtf8("switchStackShow1Btn"))
        self.gridLayout.addWidget(self.switchStackShow1Btn, 6, 0, 1, 1)
        self.switchStackShow2Btn = QtGui.QRadioButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Optima"))
        font.setPointSize(14)
        self.switchStackShow2Btn.setFont(font)
        self.switchStackShow2Btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.switchStackShow2Btn.setAutoFillBackground(True)
        self.switchStackShow2Btn.setObjectName(_fromUtf8("switchStackShow2Btn"))
        self.gridLayout.addWidget(self.switchStackShow2Btn, 6, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1337, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFILE = QtGui.QMenu(self.menubar)
        self.menuFILE.setObjectName(_fromUtf8("menuFILE"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionLOAD_NXS = QtGui.QAction(MainWindow)
        self.actionLOAD_NXS.setObjectName(_fromUtf8("actionLOAD_NXS"))
        self.actionSAVE_TIFF = QtGui.QAction(MainWindow)
        self.actionSAVE_TIFF.setObjectName(_fromUtf8("actionSAVE_TIFF"))
        self.actionQUIT = QtGui.QAction(MainWindow)
        self.actionQUIT.setObjectName(_fromUtf8("actionQUIT"))
        self.menuFILE.addSeparator()
        self.menubar.addAction(self.menuFILE.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "XPEEM data reducer", None))
        self.pickROIBtn.setText(_translate("MainWindow", "PICK-UP THE ROI", None))
        self.calcSingleSpectrumBtn.setText(_translate("MainWindow", "CALC SPECTRUM", None))
        self.load2nrjBtn.setText(_translate("MainWindow", "LOAD 2 ENERGIES", None))
        self.load2polBtn.setText(_translate("MainWindow", "LOAD 2 POLARISATIONS", None))
        self.load2XASBtn.setText(_translate("MainWindow", "LOAD 2 XAS", None))
        self.loadXASBtn.setText(_translate("MainWindow", "LOAD XAS", None))
        self.chooseWorkDirectoryBtn.setText(_translate("MainWindow", "PROCESSING DIRECTORY", None))
        self.calcDiffSpectraBtn.setText(_translate("MainWindow", "CALC DIFF SPECTRA", None))
        self.loadNormFileBtn.setText(_translate("MainWindow", "LOAD NORM", None))
        self.calcDiffImagesBtn.setText(_translate("MainWindow", "CALC DIFF IMAGES", None))
        self.plotDriftBtn.setText(_translate("MainWindow", "PLOT DRIFT", None))
        self.clearBtn.setText(_translate("MainWindow", "CLEAR VARIABLES", None))
        self.switchStackShow1Btn.setText(_translate("MainWindow", "SHOW STACK1", None))
        self.switchStackShow2Btn.setText(_translate("MainWindow", "SHOW STACK2", None))
        self.menuFILE.setTitle(_translate("MainWindow", "FILE", None))
        self.actionLOAD_NXS.setText(_translate("MainWindow", "LOAD NXS", None))
        self.actionLOAD_NXS.setToolTip(_translate("MainWindow", "LOAD NXS files", None))
        self.actionLOAD_NXS.setShortcut(_translate("MainWindow", "Ctrl+O", None))
        self.actionSAVE_TIFF.setText(_translate("MainWindow", "SAVE TIFF", None))
        self.actionQUIT.setText(_translate("MainWindow", "QUIT", None))

from pyqtgraph import ImageView, PlotWidget
