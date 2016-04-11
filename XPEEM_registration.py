# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 07:56:40 2016

@author: stanescu
"""


import os
import numpy as np
from tables import openFile
from tables.exceptions import NoSuchNodeError
from scipy import ndimage
from skimage import exposure
from skimage.feature import register_translation
import skimage.io
from multiprocessing import Pool,cpu_count


def loadHDF5(fileName):
    if fileName.endswith('.nxs'):
        nxsFile = openFile(fileName)
        nxsEntry = get_NXEntry(nxsFile)
        nxsDataParts = eval("nxsFile.root.%s.scan_data"%(nxsEntry))
        for nxsData in nxsDataParts:
            if len(nxsData.shape) == 3:
                myImgData = nxsData.read()
        if 'actuator_1_1' in nxsDataParts:
            xValues = nxsDataParts.actuator_1_1.read()
        else:
            xValues = None
        nxsFile.close()
    elif fileName.endswith('.hdf5'):
        hdf5File = openFile(fileName)
        imgIndex = 0
        myBool = True
        myImgData = []
        while myBool:
            try:
                myImgData.append(eval('hdf5File.root.entry%i.Counter0.data.read()'%(imgIndex+1)))
                imgIndex+=1
            except NoSuchNodeError:
                myBool = False
                pass
        myImgData = np.array(myImgData,dtype='int16')
        hdf5File.close()
    noSlice,imgWidth,imgHeight = np.shape(myImgData)
    return noSlice, myImgData, np.shape(myImgData),xValues


def get_NXEntry(nxsFile):
    tmp = str(nxsFile.root._g_getChildGroupClass)
    nxsEntry = eval(tmp.split()[9].strip('['))
    return nxsEntry

def loadTIFF(fileName):
    thePath = fileName[:fileName.rfind('/')]
    myImgData = []
    for imgFile in os.listdir(thePath):
        if imgFile.startswith('.'):
            pass
        else:
            imgTmp = skimage.io.imread(thePath+"/"+imgFile)
            myImgData.append(imgTmp)
    noSlice,imgWidth,imgHeight = np.shape(myImgData)
    return noSlice, myImgData, np.shape(myImgData)

def setROIregistration(myROI,myImage):
    x1,x2,y1,y2 = [myROI[0],myROI[0]+myROI[2],myROI[1],myROI[1]+myROI[3]]
    ROIimg = myImage[x1:x2,y1:y2]
    x = x2-x1
    y = y2-y1
    winFunc = makeWindow(x,y)
    ROIimg = ROIimg*winFunc
    myFilter = 'none'
    if myFilter == 'equalize':
        workImg = exposure.equalize_hist(ROIimg)
    elif myFilter == 'sobel':
        sobX = ndimage.sobel(ROIimg,axis=0,mode='constant')
        sobY = ndimage.sobel(ROIimg,axis=0,mode='constant')
        workImg = np.hypot(sobX,sobY)
    elif myFilter == 'both':
        workImg = exposure.equalize_hist(ROIimg)
        sobX = ndimage.sobel(workImg,axis=0,mode='constant')
        sobY = ndimage.sobel(workImg,axis=0,mode='constant')
        workImg = np.hypot(sobX,sobY)
    elif myFilter == 'none':
        workImg = ROIimg
    return workImg

def setDefaultROIregistration(myImage):
    imgSize = myImage.shape
    workImg = myImage[imgSize[0]*1/4:imgSize[0]*3/4,imgSize[1]*1/4:imgSize[1]*3/4]
    return workImg

def registerStack(refImg,testImg,myROI,upsamplingFactor):
    refImgROI = setROIregistration(myROI,refImg)
    #refImgROI = setDefaultROIregistration(refImg)
    testImgROI = setROIregistration(myROI,testImg)
    #testImgROI = setDefaultROIregistration(testImg)
    resReg = register_translation(refImgROI,testImgROI,upsample_factor=upsamplingFactor,space='real')
    theShifts = resReg[0]
    regImage = ndimage.shift(testImg,(theShifts[0],theShifts[1]))
    return theShifts,regImage

##################################################
###### alternative ways for registration #########

def makeWindow(x,y):
    xxyy = np.mgrid[0:x,0:y]
    return np.sin(np.pi*xxyy[0,::,::]/(x-1))*np.sin(np.pi*xxyy[1,::,::]/(y-1))

def phaseCorrelate(refImg,testImg,myROI,upsamplingFactor):
    x1,x2,y1,y2 = [myROI[0],myROI[0]+myROI[2],myROI[1],myROI[1]+myROI[3]]
    refImgROI = setROIregistration(myROI,refImg)
    testImgROI = setROIregistration(myROI,testImg)
    refImgROI = ndimage.zoom(refImgROI,upsamplingFactor)
    testImgROI = ndimage.zoom(testImgROI,upsamplingFactor)
    x = (x2-x1)*upsamplingFactor
    y = (y2-y1)*upsamplingFactor
    winFunc = makeWindow(x,y)
    imgProduct = np.fft.fft2(winFunc*refImgROI)*np.fft.fft2(winFunc*testImgROI).conj()
    resCorr = np.fft.fftshift(np.fft.ifft2(imgProduct))
    maxPos = np.unravel_index(resCorr.argmax(),resCorr.shape)
    imgSize = np.shape(refImgROI)
    if maxPos[0] >= imgSize[0]/2:
        xDrift = maxPos[0]-imgSize[0]
    else:
        xDrift = maxPos[0]
    if maxPos[1] >= imgSize[1]/2:
        yDrift = maxPos[1]-imgSize[1]
    else:
        yDrift = maxPos[1]
    driftVals = [float(xDrift)/upsamplingFactor,float(yDrift)/upsamplingFactor]
    shiftedImg = ndimage.shift(testImg,(float(xDrift)/upsamplingFactor,float(yDrift)/upsamplingFactor))
    return driftVals,shiftedImg


########## multiprocessing purposes #######################
######## here choose which drift procedure to use #########

def calc_chunk(myROI,upsamplingFactor,refImg,chunk):
    chunkResult = [registerStack(refImg,testImg,myROI,upsamplingFactor) for testImg in chunk]
    return chunkResult


###################################################

def reduce_DRIFT(noSlice,myImgStack,myShape,refImg,myROI,upsamplingFactor):
    print "No of slices => \t", noSlice
    regImg = np.zeros(myShape)
    noCPU = cpu_count()
    ImgPerChunk = noSlice/(noCPU-1)
    print "images per chunk ====> ",ImgPerChunk
    chunkList = [myImgStack[img:img+ImgPerChunk] for img in range(0,noSlice,ImgPerChunk)]
    print "no of chunks ===> ",len(chunkList)
    pool = Pool(processes=noCPU)
    print "number of processors ====> ",noCPU
    chunkedResults = [pool.apply_async(calc_chunk,args=(myROI,upsamplingFactor,refImg,chunk)) for chunk in chunkList]
    pool.close()
    pool.join()
    singleResult = [res.get() for res in chunkedResults]
    resultStack = np.concatenate(singleResult,axis=0)
    regImg = [resultStack[theIndex][1] for theIndex in range(len(resultStack))]
    shiftStack = [resultStack[theIndex][0] for theIndex in range(len(resultStack))]
    shiftX = [shiftStack[theIndex][0] for theIndex in range(len(shiftStack))]
    shiftY = [shiftStack[theIndex][1] for theIndex in range(len(shiftStack))]
    return regImg,shiftX,shiftY


def apply_Mask(myImgStack):
    imgTmp = myImgStack[0]
    lx,ly = imgTmp.shape
    X, Y = np.ogrid[0:lx, 0:ly]
    myMask = (X - lx / 2) ** 2 + (Y - ly / 2) ** 2 > lx * ly / 4.5
    for theImg in myImgStack:
        theImg[myMask] = 0

def saveSpectra(workDir,fileName,theSpectra):
    fileNameRoot = fileName[fileName.rfind('/'):].strip('/')
    np.savetxt(workDir+fileNameRoot+"_spectra.txt",np.transpose(np.array(theSpectra)))

def saveShifts(workDir,fileName,sx,sy):
    fileNameRoot = fileName[fileName.rfind('/'):].strip('/')
    np.savetxt(workDir+fileNameRoot+"_shifts.txt",np.transpose([sx,sy]))
