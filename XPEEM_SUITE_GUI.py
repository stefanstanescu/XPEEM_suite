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
import numpy as np
import sys
from PyQt4 import QtGui
import XPEEM_GUI
import XPEEM_registration as xpeem
import skimage.io

class myGUIapp(QtGui.QMainWindow,XPEEM_GUI.Ui_MainWindow):
    def __init__(self,parent=None):
        super(myGUIapp,self).__init__(parent)
        self.setupUi(self)
        self.chooseWorkDirectoryBtn.clicked.connect(self.chooseWorkDir)
        self.load1FileBtn.clicked.connect(self.load1file)
        self.load2FilesBtn.clicked.connect(self.load2files)
        self.loadNormFileBtn.clicked.connect(self.loadNormFile)
        self.showTIFFStackBtn.clicked.connect(self.showTIFF)
        self.pickROIBtn.clicked.connect(self.pickROI)
        self.UserPickedROI = False
        self.calcSingleSpectrumBtn.clicked.connect(self.calcSingleSpectrum)
        self.calcDiffSpectraBtn.clicked.connect(self.calcDiffSpectra)
        self.calcDiffImagesBtn.clicked.connect(self.calcDiffImages)
        self.switchStackShow1Btn.toggled.connect(self.toogleStack1View)
        self.switchStackShow2Btn.toggled.connect(self.toogleStack2View)
        self.normBtn.stateChanged.connect(self.normalizeStack)
        self.calcROIBtn.stateChanged.connect(self.autoCalcROI)
        self.calcROIBtn.setChecked(True)
        
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
        
    def load1file(self):
        self.loadContext = 'ONE FILE'
        self.fileName = str(QtGui.QFileDialog.getOpenFileName(self,'Pick a DATA file','', 'NeXuS (*.nxs)'))
        self.noSlice,self.imgStack,self.myShape,self.xValues = xpeem.loadHDF5(self.fileName)
        if self.xValues == None:
            self.imageView.setImage(self.imgStack)
        else:
            self.imageView.setImage(self.imgStack,xvals=self.xValues)
        self.changeLabelText(self.fileName)
       
    def load2files(self):
        self.loadContext = 'TWO FILES'
        self.fileName1 = str(QtGui.QFileDialog.getOpenFileName(self,'Pick a DATA file','', 'NeXuS (*.nxs)'))
        self.noSlice1,self.imgStack1,self.myShape1,self.xValues1 = xpeem.loadHDF5(self.fileName1)
        if self.xValues1 == None:
            self.imageView.setImage(self.imgStack1)
        else:
            self.imageView.setImage(self.imgStack1,xvals=self.xValues1)            
        self.changeLabelText(self.fileName1)
        self.fileName2 = str(QtGui.QFileDialog.getOpenFileName(self,'Pick a DATA file','', 'NeXuS (*.nxs)'))
        self.noSlice2,self.imgStack2,self.myShape2,self.xValues2 = xpeem.loadHDF5(self.fileName2)
        if self.xValues2 == None:
            self.imageView.setImage(self.imgStack2)
        else:
            self.imageView.setImage(self.imgStack2,xvals=self.xValues2)            
        self.changeLabelText(self.fileName2)

    def loadNormFile(self):
        self.fileNameNorm = str(QtGui.QFileDialog.getOpenFileName(self,'Pick a NORMALIZATION file','', 'NeXuS (*.nxs)'))
        self.noSliceNorm,self.imgStackNorm,self.myShapeNorm,self.xValuesNorm = xpeem.loadHDF5(self.fileNameNorm)
        self.imgNorm = np.sum(self.imgStackNorm,axis=0,dtype='float32')/len(self.imgStackNorm)
        #rescaleNormFactor = (self.imgNorm.max()/min([myImg.min() for myImg in self.imgStack]))
        #self.imgNorm = self.imgNorm/rescaleNormFactor

    def toogleStack1View(self):
        if self.normBtn.isChecked():
            self.imageView.setImage(self.imgNormStack1)
            self.switchStackShow2Btn.setChecked(False)
            self.changeLabelText(self.fileName1)
        else:
            self.imageView.setImage(self.imgStack1)
            self.switchStackShow2Btn.setChecked(False)
            self.changeLabelText(self.fileName1)
            
    def toogleStack2View(self):
        if self.normBtn.isChecked():
            self.imageView.setImage(self.imgNormStack2)
            self.switchStackShow1Btn.setChecked(False)
            self.changeLabelText(self.fileName2)
        else:
            self.imageView.setImage(self.imgStack2)
            self.switchStackShow1Btn.setChecked(False)
            self.changeLabelText(self.fileName2)
            

    def calcSingleSpectrum(self):        
        if self.UserPickedROI == False:
            imageSize = self.imgNormStack[0].shape
            self.myROI = (imageSize[0]*1./4,imageSize[1]*1./4,imageSize[0]*1./2,imageSize[1]*1./2)
        else:
            self.myROI = self.myPickROI
        print "THE ROI IS ======> ",self.myROI
        upsamplingFactor = 50
        #print self.imgNorm
        if self.normBtn.isChecked():
            with open(self.workDir+'Input_Args.txt','w') as myInput:
                myInput.write(self.fileName)
                myInput.write('\n')
                myInput.write(self.fileNameNorm)
                myInput.write('\n')
                myInput.write(str(self.myROI))
                myInput.write('\n')
                myInput.write(str(upsamplingFactor))
                myInput.write('\n')
        else:
            with open(self.workDir+'Input_Args.txt','w') as myInput:
                myInput.write(self.fileName)
                myInput.write('\n')
                myInput.write(str(self.myROI))
                myInput.write('\n')
                myInput.write(str(upsamplingFactor))
                myInput.write('\n')
        os.system('python calc_single_spectrum.py '+str(self.workDir))
        self.fileNameRoot1 = self.fileName[self.fileName.rfind('/'):].strip('/')
        self.corrImgStack = skimage.io.imread(self.workDir+self.fileNameRoot1+'_CORR_stack.tif')
        if self.xValues == None:
            self.imageView.setImage(self.corrImgStack)
        else:
            self.imageView.setImage(self.corrImgStack,xvals=self.xValues)
        print "CALCULATION DONE!!!"
        self.plotDrift()
        self.actualFileName.setText(self.myRootFileName+" -------> CALC DONE!")

    def calcDiffSpectra(self):
        if self.UserPickedROI == False:
            imageSize = self.imgNormStack1[0].shape
            self.myROI = (imageSize[0]*1./4,imageSize[1]*1./4,imageSize[0]*1./2,imageSize[1]*1./2)
        else:
            self.myROI = self.myPickROI
        print "THE ROI IS ======> ",self.myROI
        upsamplingFactor = 50
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
                myInput.write(str(upsamplingFactor))
                myInput.write('\n')
        else:
            with open(self.workDir+'Input_Args.txt','w') as myInput:
                myInput.write(self.fileName1)
                myInput.write('\n')
                myInput.write(self.fileName2)
                myInput.write('\n')
                myInput.write(str(self.myROI))
                myInput.write('\n')
                myInput.write(str(upsamplingFactor))
                myInput.write('\n')
        os.system('python calc_DIFF_spectra.py '+str(self.workDir))
        self.fileNameRoot1 = self.fileName1[self.fileName1.rfind('/'):].strip('/')
        self.corrDiffStack = skimage.io.imread(self.workDir+self.fileNameRoot1+'_DIFF_stack.tif')
        if self.xValues1 == None:
            self.imageView.setImage(self.corrDiffStack)
        else:
            self.imageView.setImage(self.corrDiffStack,xvals=self.xValues1)
        print "CALCULATION DONE!!!"
        self.plotDrift()
        self.actualFileName.setText(self.myRootFileName+" -------> CALC DONE!")

    def calcDiffImages(self):
        if self.UserPickedROI == False:
            imageSize = self.imgNormStack1[0].shape
            self.myROI = (imageSize[0]*1./4,imageSize[1]*1./4,imageSize[0]*1./2,imageSize[1]*1./2)
        else:
            self.myROI = self.myPickROI
        print "THE ROI IS ======> ",self.myROI
        upsamplingFactor = 50
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
                myInput.write(str(upsamplingFactor))
                myInput.write('\n')
        else:
            with open(self.workDir+'Input_Args.txt','w') as myInput:
                myInput.write(self.fileName1)
                myInput.write('\n')
                myInput.write(self.fileName2)
                myInput.write('\n')
                myInput.write(str(self.myROI))
                myInput.write('\n')
                myInput.write(str(upsamplingFactor))
                myInput.write('\n')
        os.system('python calc_DIFF_images.py '+str(self.workDir))
        self.fileNameRoot1 = self.fileName1[self.fileName1.rfind('/'):].strip('/')
        self.corrDiffImg = skimage.io.imread(self.workDir+self.fileNameRoot1+'_DIFF_img.tif')
        self.imageView.setImage(self.corrDiffImg)
        print "CALCULATION DONE!!!"
        self.plotDrift()
        self.actualFileName.setText(self.myRootFileName+" -------> CALC DONE!")
        
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
            

    def clearVariables(self):
        varList = ['self.fileName',
                   'self.fileName1',
                   'self.fileName2',
                   'self.fileNameNorm',
                   'self.imgStack',
                   'self.imgStack1',
                   'self.imgStack2',
                   'self.imgNorm',
                   'self.imgNormStack',
                   'self.imgNormStack1',
                   'self.imgNormStack2',
                   'self.myROI',
                   'self.myShape',
                   'self.myShape1',
                   'self.myShape2',
                   'self.corrImgStack',
                   'self.corrDiffImg',
                   'self.corrDiffStack',
                   'self.noSliceNorm',
                   'self.imgStackNorm',
                   'self.myShapeNorm',
                   'self.sxsy',
                   'tiffFileName',
                   ]
        for myVar in varList:
            exec('%s = None'%myVar)
        
def main():		
    app = QtGui.QApplication(sys.argv)
    win = myGUIapp()
    win.show()
    app.exec_()

if __name__=='__main__':
    main()