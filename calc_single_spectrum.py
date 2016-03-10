# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 08:00:26 2016

@author: stanescu
"""

import sys
import numpy as np
import XPEEM_registration as xpeemreg
import skimage.io


def calc_single_spectrum(*args):
    if len(args) == 3:
        noSlice,myImgStack,myShape,xValues = xpeemreg.loadHDF5(args[0]) 
        refImg = myImgStack[0]            
        regImg,shiftX,shiftY = xpeemreg.reduce_DRIFT(noSlice,myImgStack,myShape,refImg,args[1],args[2])    
    elif len(args) == 4:
        noSlice,myImgStack,myShapexValues = xpeemreg.loadHDF5(args[0]) 
        refImg = myImgStack[0]            
        noSliceNorm,imgStackNorm,myShapeNorm = xpeemreg.loadHDF5(args[1])
        imgNorm = np.sum(imgStackNorm,axis=0,dtype='float32')/len(imgStackNorm)
        imgNormStack = [myImgStack[theSlice].astype('float32')/imgNorm for theSlice in range(noSlice)]
        imgNormStack = np.array(imgNormStack)
        regImg,shiftX,shiftY = xpeemreg.reduce_DRIFT(noSlice,imgNormStack,myShape,refImg,args[2],args[3])   
    return myImgStack,regImg,shiftX,shiftY 

def main():
    workDir = sys.argv[1]
    with open(workDir+'Input_Args.txt','r') as inputFile:
        lines = inputFile.readlines()
        if len(lines) == 3:
            fileName = lines[0].strip('\n')
            myROI = eval(lines[1])
            upsamplingFactor = eval(lines[2])
            rawStack,corrStack,sx,sy = calc_single_spectrum(fileName,myROI,upsamplingFactor)
        elif len(lines) == 4:
            fileName = lines[0].strip('\n')
            fileNameNorm = lines[1].strip('\n')
            myROI = eval(lines[2])
            upsamplingFactor = eval(lines[3])
            rawStack,corrStack,sx,sy = calc_single_spectrum(fileName,fileNameNorm,myROI,upsamplingFactor)
        
    fileNameRoot = fileName[fileName.rfind('/'):].strip('/')
    #xpeemreg.apply_Mask(rawStack)
    #xpeemreg.apply_Mask(corrStack)
    skimage.io.imsave(workDir+fileNameRoot+'_RAW_stack.tif',rawStack)
    skimage.io.imsave(workDir+fileNameRoot+'_CORR_stack.tif',corrStack)
    xpeemreg.saveShifts(workDir,fileName,sx,sy)
    

if __name__=='__main__':
    main()
   