# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 14:17:46 2016

@author: stanescu
"""


import sys
import numpy as np
import XPEEM_registration as xpeemreg
import skimage.io


def calc_ABS_NORM_DIFF_images(*args):
    if len(args) == 6:
        noSlice1,myImgStack1,myShape1,xValues1 = xpeemreg.loadHDF5(args[0])
        noSlice2,myImgStack2,myShape2,xValues2 = xpeemreg.loadHDF5(args[1])
        noSlice3,myImgStack3,myShape3,xValues3 = xpeemreg.loadHDF5(args[2])
        noSlice4,myImgStack4,myShape4,xValues4 = xpeemreg.loadHDF5(args[3])
        noSlice = noSlice1+noSlice2+noSlice3+noSlice4
        myImgStack = np.concatenate((myImgStack1,myImgStack2,myImgStack3,myImgStack4),axis=0)
        myShape = np.shape(myImgStack)
        refImg = myImgStack[0]
        regImg,shiftX,shiftY = xpeemreg.reduce_DRIFT(noSlice,myImgStack,myShape,refImg,args[4],args[5])
    elif len(args) == 7:
        noSlice1,myImgStack1,myShape1,xValues1 = xpeemreg.loadHDF5(args[0])
        noSlice2,myImgStack2,myShape2,xValues2 = xpeemreg.loadHDF5(args[1])
        noSlice3,myImgStack3,myShape3,xValues3 = xpeemreg.loadHDF5(args[2])
        noSlice4,myImgStack4,myShape4,xValues4 = xpeemreg.loadHDF5(args[3])
        noSlice = noSlice1+noSlice2+noSlice3+noSlice4
        myImgStack = np.concatenate((myImgStack1,myImgStack2,myImgStack3,myImgStack4),axis=0)
        myShape = np.shape(myImgStack)
        refImg = myImgStack[0]
        noSliceNorm,imgStackNorm,myShapeNorm,xValuesNorm = xpeemreg.loadHDF5(args[4])
        imgNorm = np.sum(imgStackNorm,axis=0,dtype='float32')/len(imgStackNorm)
        imgNormStack = [myImgStack[theSlice].astype('float32')/imgNorm for theSlice in range(noSlice)]
        imgNormStack = np.array(imgNormStack)
        regImg,shiftX,shiftY = xpeemreg.reduce_DRIFT(noSlice,imgNormStack,myShape,refImg,args[5],args[6])
    regImg1 = regImg[:noSlice/4]
    regImg2 = regImg[noSlice/4:2*noSlice/4]
    regImg3 = regImg[2*noSlice/4:3*noSlice/4]
    regImg4 = regImg[3*noSlice/4:]
    regImgSum1 = np.sum(regImg1,axis=0,dtype='float32')/(noSlice/4)
    regImgSum2 = np.sum(regImg2,axis=0,dtype='float32')/(noSlice/4)
    regImgSum3 = np.sum(regImg3,axis=0,dtype='float32')/(noSlice/4)
    regImgSum4 = np.sum(regImg4,axis=0,dtype='float32')/(noSlice/4)
    diffImgArray = ((regImgSum2-regImgSum1)/(regImgSum2+regImgSum1)-(regImgSum4-regImgSum3)/(regImgSum4+regImgSum3))
    return myImgStack[:noSlice/4],myImgStack[noSlice/4:2*noSlice/4],myImgStack[2*noSlice/4:3*noSlice/4],myImgStack[3*noSlice/4:],regImgSum1,regImgSum2,regImgSum3,regImgSum4, diffImgArray,shiftX,shiftY


def main():
    workDir = sys.argv[1]
    with open(workDir+'Input_Args.txt','r') as inputFile:
        lines = inputFile.readlines()
        if len(lines) == 6:
            fileName1 = lines[0].strip('\n')
            fileName2 = lines[1].strip('\n')
            fileName3 = lines[2].strip('\n')
            fileName4 = lines[3].strip('\n')
            myROI = eval(lines[4])
            upsamplingFactor = eval(lines[5])
            rawStack1,rawStack2,rawStack3,rawStack4,sumImg1,sumImg2,sumImg3,sumImg4,diffImg,sx,sy = calc_ABS_NORM_DIFF_images(fileName1,fileName2,fileName3,fileName4,myROI,upsamplingFactor)
        elif len(lines) == 7:
            fileName1 = lines[0].strip('\n')
            fileName2 = lines[1].strip('\n')
            fileName3 = lines[2].strip('\n')
            fileName4 = lines[3].strip('\n')
            fileNameNorm = lines[4].strip('\n')
            myROI = eval(lines[5])
            upsamplingFactor = eval(lines[6])
            rawStack1,rawStack2,rawStack3,rawStack4,sumImg1,sumImg2,sumImg3,sumImg4,diffImg,sx,sy = calc_ABS_NORM_DIFF_images(fileName1,fileName2,fileName3,fileName4,fileNameNorm,myROI,upsamplingFactor)

    fileNameRoot1 = fileName1[fileName1.rfind('/'):].strip('/')
    fileNameRoot2 = fileName2[fileName2.rfind('/'):].strip('/')
    fileNameRoot3 = fileName3[fileName3.rfind('/'):].strip('/')
    fileNameRoot4 = fileName4[fileName4.rfind('/'):].strip('/')
    skimage.io.imsave(workDir+fileNameRoot1+'_RAW_stack1.tif',rawStack1)
    skimage.io.imsave(workDir+fileNameRoot2+'_RAW_stack2.tif',rawStack2)
    skimage.io.imsave(workDir+fileNameRoot3+'_RAW_stack3.tif',rawStack3)
    skimage.io.imsave(workDir+fileNameRoot4+'_RAW_stack4.tif',rawStack4)
    skimage.io.imsave(workDir+fileNameRoot1+'_CORR1.tif',np.array(sumImg1))
    skimage.io.imsave(workDir+fileNameRoot2+'_CORR2.tif',np.array(sumImg2))
    skimage.io.imsave(workDir+fileNameRoot3+'_CORR3.tif',np.array(sumImg3))
    skimage.io.imsave(workDir+fileNameRoot4+'_CORR4.tif',np.array(sumImg4))
    skimage.io.imsave(workDir+fileNameRoot1+'_DIFF.tif',np.array(diffImg))
    xpeemreg.saveShifts(workDir,fileName1,sx,sy)


if __name__=='__main__':
    main()
