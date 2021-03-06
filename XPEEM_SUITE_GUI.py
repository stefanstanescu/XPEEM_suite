# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 17:37:43 2016

@author: stanescu
XPEEM SUITE GUI
"""

__author__ = "Stefan Stanescu"
__copyright__ = "Copyright 2016, HERMES beamline"
__credits__ = ["Stefan Stanescu"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Stefan Stanescu"
__email__ = "stefan.stanescu@synchrotron-soleil.fr"
__status__ = "Production"

import os
import platform
import numpy as np
import sys
from PyQt4 import QtGui,QtCore
import XPEEM_GUI
import XPEEM_registration as xpeem
import skimage.io
import time

#sys.path.append('C:\Anaconda2\Scripts\XPEEM_data_reducer\\')

check_platform = platform.system()

if check_platform == "Darwin":
    scripts_path = os.getcwd()+"/"
elif check_platform == "Windows":
    scripts_path = os.getcwd()+"\\"
elif check_platform == "Linux":
    scripts_path = os.getcwd()+"/"

class myGUIapp(QtGui.QMainWindow,XPEEM_GUI.Ui_MainWindow):
    def __init__(self,parent=None):
        super(myGUIapp,self).__init__(parent)
        self.setupUi(self)
        self.chooseWorkDirectoryBtn.clicked.connect(self.chooseWorkDir)
        self.load1FileBtn.clicked.connect(self.load1file)
        self.load2FilesBtn.clicked.connect(self.load2files)
        self.load4FilesBtn.clicked.connect(self.load4files)
        self.loadNormFileBtn.clicked.connect(self.loadNormFile)
        self.showTIFFStackBtn.clicked.connect(self.showTIFF)
        self.pickROIBtn.clicked.connect(self.pickROI)
        self.UserPickedROI = False
        self.calcSingleSpectrumBtn.clicked.connect(self.calcSingleSpectrum)
        self.calcDiffSpectraBtn.clicked.connect(self.calcDiffSpectra)
        self.calcDiffImagesBtn.clicked.connect(self.calcDiffImages)
        self.calcDiff4ImagesBtn.clicked.connect(self.calcAbsNormDiffImages)
        self.switchStackShow1Btn.toggled.connect(self.toogleStack1View)
        self.switchStackShow2Btn.toggled.connect(self.toogleStack2View)
        self.normBtn.stateChanged.connect(self.normalizeStack)
        self.normBtn.setChecked(False)
        self.calcROIBtn.stateChanged.connect(self.autoCalcROI)
        self.calcROIBtn.setChecked(False)
        self.imageView.roi.sigRegionChanged.disconnect()
        self.calcTimer = QtCore.QTimer()
        self.calcTimer.timeout.connect(self.countdown)
        self.dataDirectory = ""

    def countdown(self):
        mytime = time.time()-self.initTime
        self.lcdTimer.display(mytime)
        time.sleep(0.1)

    def chooseWorkDir(self):
        self.workDir = str(QtGui.QFileDialog.getExistingDirectory(self,"Select your working directory"))+'/'

    def pickROI(self):
        self.UserPickedROI = True
        self.ROIposition = self.imageView.roi.pos()
        self.ROIsize = self.imageView.roi.size()
        self.myPickROI = (np.int(self.ROIposition[0]),np.int(self.ROIposition[1]),np.int(self.ROIsize[0]),np.int(self.ROIsize[1]))

    def normalizeStack(self):
        if self.loadContext == 'ONE FILE':
            if self.normBtn.isChecked():
                self.imgNorm = np.sum(self.imgStackNorm,axis=0,dtype='float32')/len(self.imgStackNorm)
                self.imgNormStack = [self.imgStack[theSlice].astype('float32')/self.imgNorm for theSlice in range(self.noSlice)]
                self.imgNormStack = np.array(self.imgNormStack)
                if self.xValues == None:
                    self.imageView.setImage(self.imgNormStack)
                else:
                    self.imageView.setImage(self.imgNormStack,xvals=self.xValues)
            else:
                self.imgNormStack = self.imgStack
                if self.xValues == None:
                    self.imageView.setImage(self.imgNormStack)
                else:
                    self.imageView.setImage(self.imgNormStack,xvals=self.xValues)
        elif self.loadContext == 'TWO FILES':
            if self.normBtn.isChecked():
                self.imgNorm = np.sum(self.imgStackNorm,axis=0,dtype='float32')/len(self.imgStackNorm)
                self.imgNormStack1 = [self.imgStack1[theSlice1].astype('float32')/self.imgNorm for theSlice1 in range(self.noSlice1)]
                self.imgNormStack1 = np.array(self.imgNormStack1)
                self.imgNormStack2 = [self.imgStack2[theSlice2].astype('float32')/self.imgNorm for theSlice2 in range(self.noSlice2)]
                self.imgNormStack2 = np.array(self.imgNormStack2)
                if self.xValues2 == None:
                    self.imageView.setImage(self.imgNormStack2)
                else:
                    self.imageView.setImage(self.imgNormStack2,xvals=self.xValues2)
            else:
                self.imgNormStack1 = self.imgStack1
                self.imgNormStack2 = self.imgStack2
                if self.xValues2 == None:
                    self.imageView.setImage(self.imgNormStack2)
                else:
                    self.imageView.setImage(self.imgNormStack2,xvals=self.xValues2)
        elif self.loadContext == 'FOUR FILES':
            if self.normBtn.isChecked():
                self.imgNorm = np.sum(self.imgStackNorm,axis=0,dtype='float32')/len(self.imgStackNorm)
                self.imgNormStack1 = [self.imgStack1[theSlice1].astype('float32')/self.imgNorm for theSlice1 in range(self.noSlice1)]
                self.imgNormStack1 = np.array(self.imgNormStack1)
                self.imgNormStack2 = [self.imgStack2[theSlice2].astype('float32')/self.imgNorm for theSlice2 in range(self.noSlice2)]
                self.imgNormStack2 = np.array(self.imgNormStack2)
                self.imgNormStack3 = [self.imgStack3[theSlice3].astype('float32')/self.imgNorm for theSlice3 in range(self.noSlice3)]
                self.imgNormStack3 = np.array(self.imgNormStack3)
                self.imgNormStack4 = [self.imgStack4[theSlice4].astype('float32')/self.imgNorm for theSlice4 in range(self.noSlice4)]
                self.imgNormStack4 = np.array(self.imgNormStack4)
                if self.xValues4 == None:
                    self.imageView.setImage(self.imgNormStack4)
                else:
                    self.imageView.setImage(self.imgNormStack4,xvals=self.xValues4)
            else:
                self.imgNormStack1 = self.imgStack1
                self.imgNormStack2 = self.imgStack2
                self.imgNormStack3 = self.imgStack3
                self.imgNormStack4 = self.imgStack4
                if self.xValues4 == None:
                    self.imageView.setImage(self.imgNormStack4)
                else:
                    self.imageView.setImage(self.imgNormStack4,xvals=self.xValues4)

    def load1file(self):
        self.loadContext = 'ONE FILE'
        self.fileName = str(QtGui.QFileDialog.getOpenFileName(self,'Pick a DATA file',self.dataDirectory, 'NeXuS HDF5 (*.nxs *.hdf5)'))
        self.noSlice,self.imgStack,self.myShape,self.xValues = xpeem.loadHDF5(self.fileName)
        if self.xValues == None:
            self.imageView.setImage(self.imgStack)
        else:
            self.imageView.setImage(self.imgStack,xvals=self.xValues)
        self.changeLabelText(self.fileName)

    def load2files(self):
        self.loadContext = 'TWO FILES'
        self.fileName1 = str(QtGui.QFileDialog.getOpenFileName(self,'Pick a DATA file',self.dataDirectory, 'NeXuS (*.nxs)'))
        self.noSlice1,self.imgStack1,self.myShape1,self.xValues1 = xpeem.loadHDF5(self.fileName1)
        if self.xValues1 == None:
            self.imageView.setImage(self.imgStack1)
        else:
            self.imageView.setImage(self.imgStack1,xvals=self.xValues1)
        self.changeLabelText(self.fileName1)
        self.fileName2 = str(QtGui.QFileDialog.getOpenFileName(self,'Pick a DATA file',self.dataDirectory, 'NeXuS (*.nxs)'))
        self.noSlice2,self.imgStack2,self.myShape2,self.xValues2 = xpeem.loadHDF5(self.fileName2)
        if self.xValues2 == None:
            self.imageView.setImage(self.imgStack2)
        else:
            self.imageView.setImage(self.imgStack2,xvals=self.xValues2)
        self.changeLabelText(self.fileName2)

    def load4files(self):
        self.loadContext = 'FOUR FILES'
        self.fileName1 = str(QtGui.QFileDialog.getOpenFileName(self,'Pick a DATA file',self.dataDirectory, 'NeXuS (*.nxs)'))
        self.noSlice1,self.imgStack1,self.myShape1,self.xValues1 = xpeem.loadHDF5(self.fileName1)
        if self.xValues1 == None:
            self.imageView.setImage(self.imgStack1)
        else:
            self.imageView.setImage(self.imgStack1,xvals=self.xValues1)
        self.changeLabelText(self.fileName1)
        self.fileName2 = str(QtGui.QFileDialog.getOpenFileName(self,'Pick a DATA file',self.dataDirectory, 'NeXuS (*.nxs)'))
        self.noSlice2,self.imgStack2,self.myShape2,self.xValues2 = xpeem.loadHDF5(self.fileName2)
        if self.xValues2 == None:
            self.imageView.setImage(self.imgStack2)
        else:
            self.imageView.setImage(self.imgStack2,xvals=self.xValues2)
        self.changeLabelText(self.fileName2)
        self.fileName3 = str(QtGui.QFileDialog.getOpenFileName(self,'Pick a DATA file',self.dataDirectory, 'NeXuS (*.nxs)'))
        self.noSlice3,self.imgStack3,self.myShape3,self.xValues3 = xpeem.loadHDF5(self.fileName3)
        if self.xValues3 == None:
            self.imageView.setImage(self.imgStack3)
        else:
            self.imageView.setImage(self.imgStack3,xvals=self.xValues3)
        self.changeLabelText(self.fileName3)
        self.fileName4 = str(QtGui.QFileDialog.getOpenFileName(self,'Pick a DATA file',self.dataDirectory, 'NeXuS (*.nxs)'))
        self.noSlice4,self.imgStack4,self.myShape4,self.xValues4 = xpeem.loadHDF5(self.fileName4)
        if self.xValues4 == None:
            self.imageView.setImage(self.imgStack4)
        else:
            self.imageView.setImage(self.imgStack4,xvals=self.xValues4)
        self.changeLabelText(self.fileName4)

    def loadNormFile(self):
        self.fileNameNorm = str(QtGui.QFileDialog.getOpenFileName(self,'Pick a NORMALIZATION file',self.dataDirectory, 'NeXuS (*.nxs)'))
        self.noSliceNorm,self.imgStackNorm,self.myShapeNorm,self.xValuesNorm = xpeem.loadHDF5(self.fileNameNorm)
        self.imgNorm = np.sum(self.imgStackNorm,axis=0,dtype='float32')/len(self.imgStackNorm)
        #rescaleNormFactor = (self.imgNorm.max()/min([myImg.min() for myImg in self.imgStack]))
        #self.imgNorm = self.imgNorm/rescaleNormFactor

    def toogleStack1View(self):
        self.corrStack1 = skimage.io.imread(self.workDir+self.fileNameRoot1+'_CORR1.tif')
        if self.xValues1 == None:
            self.imageView.setImage(self.corrStack1)
        else:
            self.imageView.setImage(self.corrStack1,xvals=self.xValues1)
        self.switchStackShow2Btn.setChecked(False)
        self.changeLabelText(self.fileName1)

    def toogleStack2View(self):
        self.corrDiffStack = skimage.io.imread(self.workDir+self.fileNameRoot1+'_DIFF.tif')
        if self.xValues1 == None:
            self.imageView.setImage(self.corrDiffStack)
        else:
            self.imageView.setImage(self.corrDiffStack,xvals=self.xValues1)
        self.switchStackShow1Btn.setChecked(False)
        self.changeLabelText(self.fileName2)


    def calcSingleSpectrum(self):
        self.initTime  = time.time()
        self.calcTimer.start()
        if self.UserPickedROI == False:
            self.normalizeStack()
            imageSize = self.imgNormStack[0].shape
            self.myROI = (imageSize[0]*1./4,imageSize[1]*1./4,imageSize[0]*1./2,imageSize[1]*1./2)
        else:
            self.myROI = self.myPickROI
        print "THE ROI IS ======> ",self.myROI
        self.upsamplingFactor = self.upsamplingLine.text()
        #print self.imgNorm
        if self.normBtn.isChecked():
            with open(self.workDir+'Input_Args.txt','w') as myInput:
                myInput.write(self.fileName)
                myInput.write('\n')
                myInput.write(self.fileNameNorm)
                myInput.write('\n')
                myInput.write(str(self.myROI))
                myInput.write('\n')
                myInput.write(str(self.upsamplingFactor))
                myInput.write('\n')
        else:
            with open(self.workDir+'Input_Args.txt','w') as myInput:
                myInput.write(self.fileName)
                myInput.write('\n')
                myInput.write(str(self.myROI))
                myInput.write('\n')
                myInput.write(str(self.upsamplingFactor))
                myInput.write('\n')
        os.system('python ' + scripts_path + 'calc_single_spectrum.py '+str(self.workDir))
        self.fileNameRoot1 = self.fileName[self.fileName.rfind('/'):].strip('/')
        self.corrImgStack = skimage.io.imread(self.workDir+self.fileNameRoot1+'_CORR1.tif')
        if self.xValues == None:
            self.imageView.setImage(self.corrImgStack)
        else:
            self.imageView.setImage(self.corrImgStack,xvals=self.xValues)
        print "CALCULATION DONE!!!"
        self.plotDrift()
        self.actualFileName.setText(self.myRootFileName+" -------> CALC DONE!")
        self.calcTimer.stop()
        #self.switchStackShow1Btn.setChecked(False)
        #self.switchStackShow2Btn.setChecked(True)

    def calcDiffSpectra(self):
        self.initTime  = time.time()
        self.calcTimer.start()
        if self.UserPickedROI == False:
            self.normalizeStack()
            imageSize = self.imgNormStack1[0].shape
            self.myROI = (imageSize[0]*1./4,imageSize[1]*1./4,imageSize[0]*1./2,imageSize[1]*1./2)
        else:
            self.myROI = self.myPickROI
        print "THE ROI IS ======> ",self.myROI
        self.upsamplingFactor = self.upsamplingLine.text()
        #print self.imgNorm
        if self.normBtn.isChecked():
            with open(self.workDir+'Input_Args.txt','w') as myInput:
                myInput.write(self.fileName1)
                myInput.write('\n')
                myInput.write(self.fileName2)
                myInput.write('\n')
                myInput.write(self.fileNameNorm)
                myInput.write('\n')
                myInput.write(str(self.myROI))
                myInput.write('\n')
                myInput.write(str(self.upsamplingFactor))
                myInput.write('\n')
        else:
            with open(self.workDir+'Input_Args.txt','w') as myInput:
                myInput.write(self.fileName1)
                myInput.write('\n')
                myInput.write(self.fileName2)
                myInput.write('\n')
                myInput.write(str(self.myROI))
                myInput.write('\n')
                myInput.write(str(self.upsamplingFactor))
                myInput.write('\n')
        os.system('python ' + scripts_path + 'calc_DIFF_spectra.py '+str(self.workDir))
        self.fileNameRoot1 = self.fileName1[self.fileName1.rfind('/'):].strip('/')
        self.corrDiffStack = skimage.io.imread(self.workDir+self.fileNameRoot1+'_DIFF.tif')
        if self.xValues1 == None:
            self.imageView.setImage(self.corrDiffStack)
        else:
            self.imageView.setImage(self.corrDiffStack,xvals=self.xValues1)
        print "CALCULATION DONE!!!"
        self.plotDrift()
        self.actualFileName.setText(self.myRootFileName+" -------> CALC DONE!")
        self.switchStackShow1Btn.setChecked(False)
        self.switchStackShow2Btn.setChecked(True)
        self.calcTimer.stop()


    def calcDiffImages(self):
        self.initTime  = time.time()
        self.calcTimer.start()
        if self.UserPickedROI == False:
            self.normalizeStack()
            imageSize = self.imgNormStack1[0].shape
            self.myROI = (imageSize[0]*1./4,imageSize[1]*1./4,imageSize[0]*1./2,imageSize[1]*1./2)
        else:
            self.myROI = self.myPickROI
        print "THE ROI IS ======> ",self.myROI
        self.upsamplingFactor = self.upsamplingLine.text()
        #print self.imgNorm
        if self.normBtn.isChecked():
            with open(self.workDir+'Input_Args.txt','w') as myInput:
                myInput.write(self.fileName1)
                myInput.write('\n')
                myInput.write(self.fileName2)
                myInput.write('\n')
                myInput.write(self.fileNameNorm)
                myInput.write('\n')
                myInput.write(str(self.myROI))
                myInput.write('\n')
                myInput.write(str(self.upsamplingFactor))
                myInput.write('\n')
        else:
            with open(self.workDir+'Input_Args.txt','w') as myInput:
                myInput.write(self.fileName1)
                myInput.write('\n')
                myInput.write(self.fileName2)
                myInput.write('\n')
                myInput.write(str(self.myROI))
                myInput.write('\n')
                myInput.write(str(self.upsamplingFactor))
                myInput.write('\n')
        os.system('python ' + scripts_path + 'calc_DIFF_images.py '+str(self.workDir))
        self.fileNameRoot1 = self.fileName1[self.fileName1.rfind('/'):].strip('/')
        self.corrDiffImg = skimage.io.imread(self.workDir+self.fileNameRoot1+'_DIFF.tif')
        self.imageView.setImage(self.corrDiffImg)
        print "CALCULATION DONE!!!"
        self.plotDrift()
        self.actualFileName.setText(self.myRootFileName+" -------> CALC DONE!")
        self.switchStackShow1Btn.setChecked(False)
        self.switchStackShow2Btn.setChecked(True)
        self.calcTimer.stop()

    def calcAbsNormDiffImages(self):
        self.initTime  = time.time()
        self.calcTimer.start()
        if self.UserPickedROI == False:
            self.normalizeStack()
            imageSize = self.imgNormStack1[0].shape
            self.myROI = (imageSize[0]*1./4,imageSize[1]*1./4,imageSize[0]*1./2,imageSize[1]*1./2)
        else:
            self.myROI = self.myPickROI
        print "THE ROI IS ======> ",self.myROI
        self.upsamplingFactor = self.upsamplingLine.text()
        #print self.imgNorm
        if self.normBtn.isChecked():
            with open(self.workDir+'Input_Args.txt','w') as myInput:
                myInput.write(self.fileName1)
                myInput.write('\n')
                myInput.write(self.fileName2)
                myInput.write('\n')
                myInput.write(self.fileName3)
                myInput.write('\n')
                myInput.write(self.fileName4)
                myInput.write('\n')
                myInput.write(self.fileNameNorm)
                myInput.write('\n')
                myInput.write(str(self.myROI))
                myInput.write('\n')
                myInput.write(str(self.upsamplingFactor))
                myInput.write('\n')
        else:
            with open(self.workDir+'Input_Args.txt','w') as myInput:
                myInput.write(self.fileName1)
                myInput.write('\n')
                myInput.write(self.fileName2)
                myInput.write('\n')
                myInput.write(self.fileName3)
                myInput.write('\n')
                myInput.write(self.fileName4)
                myInput.write('\n')
                myInput.write(str(self.myROI))
                myInput.write('\n')
                myInput.write(str(self.upsamplingFactor))
                myInput.write('\n')
        os.system('python ' + scripts_path + 'calc_ABS_NORM_DIFF_images.py '+str(self.workDir))
        self.fileNameRoot1 = self.fileName1[self.fileName1.rfind('/'):].strip('/')
        self.corrDiffImg = skimage.io.imread(self.workDir+self.fileNameRoot1+'_DIFF.tif')
        self.imageView.setImage(self.corrDiffImg)
        print "CALCULATION DONE!!!"
        self.plotDrift()
        self.actualFileName.setText(self.myRootFileName+" -------> CALC DONE!")
        self.switchStackShow1Btn.setChecked(False)
        self.switchStackShow2Btn.setChecked(True)
        self.calcTimer.stop()

    def plotDrift(self):
        self.plotView.clear()
        self.sxsy = np.loadtxt(self.workDir+self.fileNameRoot1+"_shifts.txt")
        self.plotView.plot(self.sxsy[:,0],self.sxsy[:,1])

    def showTIFF(self):
        self.tiffFileName = str(QtGui.QFileDialog.getOpenFileName(self,'Pick a TIFF file',self.workDir,'Images (*.tif)'))
        tiffImg = skimage.io.imread(self.tiffFileName)
        self.imageView.setImage(tiffImg)
        self.changeLabelText(self.tiffFileName)

    def changeLabelText(self,myFileName):
        self.myRootFileName = myFileName[myFileName.rfind('/'):].strip('/')
        self.actualFileName.setText(self.myRootFileName)

    def autoCalcROI(self):
        #self.imageView.roi.pos()
        if self.calcROIBtn.isChecked():
            self.imageView.roi.sigRegionChanged.connect(self.imageView.roiChanged)
        else:
            self.imageView.roi.sigRegionChanged.disconnect()

def main():
    app = QtGui.QApplication(sys.argv)
    win = myGUIapp()
    win.show()
    app.exec_()

if __name__=='__main__':
    main()
