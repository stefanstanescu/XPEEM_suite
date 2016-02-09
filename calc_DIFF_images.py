# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 14:17:46 2016

@author: stanescu
"""


import sys
import numpy as np
import XPEEM_registration as xpeemreg
import skimage.io


def calc_DIFF_images(*args):
    noSlice1,myImgStack1,myShape1 = xpeemreg.loadHDF5(args[0])
    noSlice2,myImgStack2,myShape2 = xpeemreg.loadHDF5(args[1])
    noSlice = noSlice1+noSlice2
    myImgStack = np.concatenate((myImgStack1,myImgStack2),axis=0)    
    myShape = np.shape(myImgStack)
    refImg = myImgStack[0]
    regImg,shiftX,shiftY = xpeemreg.reduce_DRIFT(noSlice,myImgStack,myShape,refImg,args[2],args[3])    
    regImg1 = regImg[:noSlice/2]
    regImg2 = regImg[noSlice/2:]
    regImgSum1 = np.sum(regImg1,axis=0,dtype='float32')/(noSlice/2)
    regImgSum2 = np.sum(regImg2,axis=0,dtype='float32')/(noSlice/2)
    diffImgArray = (regImgSum1-regImgSum2)/(regImgSum1+regImgSum2)    
    return myImgStack[:noSlice/2],myImgStack[noSlice/2:],regImgSum1,regImgSum2,diffImgArray,shiftX,shiftY


def main():
    workDir = sys.argv[1]
    with open(workDir+'Input_Args.txt','r') as inputFile:
        lines = inputFile.readlines()
        fileName1 = lines[0].strip('\n')
        fileName2 = lines[1].strip('\n')
        myROI = eval(lines[2])
        upsamplingFactor = eval(lines[3])
    rawStack1,rawStack2,sumImg1,sumImg2,diffImg,sx,sy = calc_DIFF_images(fileName1,fileName2,myROI,upsamplingFactor)
    fileNameRoot1 = fileName1[fileName1.rfind('/'):].strip('/')
    fileNameRoot2 = fileName2[fileName2.rfind('/'):].strip('/')
    #xpeemreg.apply_Mask(rawStack1)
    #xpeemreg.apply_Mask(rawStack2)
    #xpeemreg.apply_Mask(sumImg1)
    #xpeemreg.apply_Mask(sumImg2)
    #xpeemreg.apply_Mask(diffImg)
    skimage.io.imsave(workDir+fileNameRoot1+'_RAW_stack1.tif',rawStack1)
    skimage.io.imsave(workDir+fileNameRoot2+'_RAW_stack2.tif',rawStack2)
    skimage.io.imsave(workDir+fileNameRoot1+'_CORR_SUM1.tif',sumImg1)
    skimage.io.imsave(workDir+fileNameRoot2+'_CORR_SUM2.tif',sumImg2)
    skimage.io.imsave(workDir+fileNameRoot1+'_DIFF_img.tif',diffImg)
    xpeemreg.saveShifts(workDir,fileName1,sx,sy)
    

if __name__=='__main__':
    main()
   
