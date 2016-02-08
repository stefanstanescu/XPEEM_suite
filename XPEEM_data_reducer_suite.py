# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 17:37:43 2016

@author: stanescu
XPEEM SUITE GUI
"""

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
        self.loadXASBtn.clicked.connect(self.loadXASfile)
        self.load2XASBtn.clicked.connect(self.load2XASfile)
        self.loadNormFileBtn.clicked.connect(self.loadNormFile)
        self.load2polBtn.clicked.connect(self.load2pol)
        self.load2nrjBtn.clicked.connect(self.load2nrj)
        self.imgNorm = None
        self.myPickROI = None
        self.pickROIBtn.clicked.connect(self.pickROI)
        self.calcSingleSpectrumBtn.clicked.connect(self.calcSingleSpectrum)
        self.calcDiffSpectraBtn.clicked.connect(self.calcDiffSpectra)
        self.calcDiffImagesBtn.clicked.connect(self.calcDiffImages)
        self.switchStackShow1Btn.toggled.connect(self.toogleStack1View)
        self.switchStackShow2Btn.toggled.connect(self.toogleStack2View)
        self.plotDriftBtn.clicked.connect(self.plotDrift)
        self.clearBtn.clicked.connect(self.clearVariables)
        
    def chooseWorkDir(self):
        self.workDir = str(QtGui.QFileDialog.getExistingDirectory(self,"Select your working directory"))+'/'      
        
    def pickROI(self):
        self.ROIposition = self.imageView.roi.pos()
        self.ROIsize = self.imageView.roi.size()
        self.myPickROI = (np.int(self.ROIposition[0]),np.int(self.ROIposition[1]),np.int(self.ROIsize[0]),np.int(self.ROIsize[1]))

    def loadNormFile(self):
        self.fileNameNorm = str(QtGui.QFileDialog.getOpenFileName(self,'Pick a NORMALISATION file'))
        noSliceNorm,imgStackNorm,myShapeNorm = xpeem.loadHDF5(self.fileNameNorm)
        self.imgNorm = np.sum(imgStackNorm,axis=0,dtype='float32')/len(imgStackNorm)
        rescaleNormFactor = (self.imgNorm.max()/min([myImg.min() for myImg in self.imgStack]))
        self.imgNorm = self.imgNorm/rescaleNormFactor
        
    def loadXASfile(self):
        self.fileName = str(QtGui.QFileDialog.getOpenFileName(self,'Pick a DATA file'))
        self.noSlice,self.imgStack,self.myShape = xpeem.loadHDF5(self.fileName)
        self.imageView.setImage(self.imgStack)
        if self.imgNorm == None:
            self.imgNorm = 1
        else:
            pass
        self.imgNormStack = [self.imgStack[theSlice].astype('float32')/self.imgNorm for theSlice in range(self.noSlice)]
        self.imgNormStack = np.array(self.imgNormStack)
        self.imageView.setImage(self.imgNormStack)
       
    def load2XASfile(self):
        self.fileName1 = str(QtGui.QFileDialog.getOpenFileName(self,'Pick first DATA file'))
        self.noSlice1,self.imgStack1,self.myShape1 = xpeem.loadHDF5(self.fileName1)
        self.imageView.setImage(self.imgStack1)
        self.fileName2 = str(QtGui.QFileDialog.getOpenFileName(self,'Pick second DATA file'))
        self.noSlice2,self.imgStack2,self.myShape2 = xpeem.loadHDF5(self.fileName2)
        self.imageView.setImage(self.imgStack2)
        if self.imgNorm == None:
            self.imgNorm = 1
        else:
            pass
        self.imgNormStack1 = [self.imgStack1[theSlice1].astype('float32')/self.imgNorm for theSlice1 in range(self.noSlice1)]
        self.imgNormStack1 = np.array(self.imgNormStack1)
        self.imgNormStack2 = [self.imgStack2[theSlice2].astype('float32')/self.imgNorm for theSlice2 in range(self.noSlice2)]
        self.imgNormStack2 = np.array(self.imgNormStack2)
        self.imageView.setImage(self.imgNormStack2)
    
    def load2pol(self):
        self.fileName1 = str(QtGui.QFileDialog.getOpenFileName(self,'Pick first DATA file'))
        self.noSlice1,self.imgStack1,self.myShape1 = xpeem.loadHDF5(self.fileName1)
        self.imageView.setImage(self.imgStack1)
        self.fileName2 = str(QtGui.QFileDialog.getOpenFileName(self,'Pick second DATA file'))
        self.noSlice2,self.imgStack2,self.myShape2 = xpeem.loadHDF5(self.fileName2)
        self.imageView.setImage(self.imgStack2)
        if self.imgNorm == None:
            self.imgNorm = 1
        else:
            pass
        self.imgNormStack1 = [self.imgStack1[theSlice1].astype('float32')/self.imgNorm for theSlice1 in range(self.noSlice1)]
        self.imgNormStack1 = np.array(self.imgNormStack1)
        self.imgNormStack2 = [self.imgStack2[theSlice2].astype('float32')/self.imgNorm for theSlice2 in range(self.noSlice2)]
        self.imgNormStack2 = np.array(self.imgNormStack2)
        self.imageView.setImage(self.imgNormStack2)        

    def load2nrj(self):
        self.fileName1 = str(QtGui.QFileDialog.getOpenFileName(self,'Pick first DATA file'))
        self.noSlice1,self.imgStack1,self.myShape1 = xpeem.loadHDF5(self.fileName1)
        self.imageView.setImage(self.imgStack1)
        self.fileName2 = str(QtGui.QFileDialog.getOpenFileName(self,'Pick second DATA file'))
        self.noSlice2,self.imgStack2,self.myShape2 = xpeem.loadHDF5(self.fileName2)
        self.imageView.setImage(self.imgStack2)
        if self.imgNorm == None:
            self.imgNorm = 1
        else:
            pass
        self.imgNormStack1 = [self.imgStack1[theSlice1].astype('float32')/self.imgNorm for theSlice1 in range(self.noSlice1)]
        self.imgNormStack1 = np.array(self.imgNormStack1)
        self.imgNormStack2 = [self.imgStack2[theSlice2].astype('float32')/self.imgNorm for theSlice2 in range(self.noSlice2)]
        self.imgNormStack2 = np.array(self.imgNormStack2)
        self.imageView.setImage(self.imgNormStack2)        

    def toogleStack1View(self):
        self.imageView.setImage(self.imgStack1)
        self.switchStackShow2Btn.setChecked(False)
    def toogleStack2View(self):
        self.imageView.setImage(self.imgStack2)
        self.switchStackShow1Btn.setChecked(False)
        

    def calcSingleSpectrum(self):
        self.myROI = self.myPickROI
        print "THE ROI IS ======> ",self.myROI
        upsamplingFactor = 50
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
        self.imageView.setImage(self.corrImgStack)


    def calcDiffSpectra(self):
        self.myROI = self.myPickROI
        print "THE ROI IS ======> ",self.myROI
        upsamplingFactor = 50
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
        self.imageView.setImage(self.corrDiffStack)

    def calcDiffImages(self):
        self.myROI = self.myPickROI
        print "THE ROI IS ======> ",self.myROI
        upsamplingFactor = 50
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
        

    def plotDrift(self):
        self.sxsy = np.loadtxt(self.workDir+self.fileNameRoot1+"_shifts.txt")
        self.plotView.plot(self.sxsy[:,0],self.sxsy[:,1])
        
    def clearVariables(self):
        #self.varList = [self.fileName,self.fileName1,self.fileName2,self.fileNameNorm,self.fileNameRoot1,self.imgStack,self.imgStack1,
                        #self.imgStack2,self.imgNorm,self.imgNormStack,self.imgNormStack1,self.imgNormStack2,self.myROI,self.myShape,
                        #self.myShape1,self.myShape2,self.corrImgStack,self.corrDiffImg,self.corrDiffStack]
        #for myVar in self.varList:
            #try:
                #del myVar
            #except:
                #pass
        print locals()

def main():		
    app = QtGui.QApplication(sys.argv)
    win = myGUIapp()
    win.show()
    app.exec_()

if __name__=='__main__':
    main()
