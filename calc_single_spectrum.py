# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 08:00:26 2016

@author: stanescu
"""

import sys
import XPEEM_registration as xpeemreg
import skimage.io


def calc_single_spectrum(*args):
    noSlice,myImgStack,myShape = xpeemreg.loadHDF5(args[0])
    refImg = myImgStack[0]    
    regImg,shiftX,shiftY = xpeemreg.reduce_DRIFT(noSlice,myImgStack,myShape,refImg,args[1],args[2])    
    return myImgStack,regImg,shiftX,shiftY 

def main():
    workDir = sys.argv[1]
    with open(workDir+'Input_Args.txt','r') as inputFile:
        lines = inputFile.readlines()
        fileName = lines[0].strip('\n')
        myROI = eval(lines[1])
        upsamplingFactor = eval(lines[2])
        rawStack,corrStack,sx,sy = calc_single_spectrum(fileName,myROI,upsamplingFactor)
            
    fileNameRoot = fileName[fileName.rfind('/'):].strip('/')
    #xpeemreg.apply_Mask(rawStack)
    #xpeemreg.apply_Mask(corrStack)
    skimage.io.imsave(workDir+fileNameRoot+'_RAW_stack.tif',rawStack)
    skimage.io.imsave(workDir+fileNameRoot+'_CORR_stack.tif',corrStack)
    xpeemreg.saveShifts(workDir,fileName,sx,sy)
    

if __name__=='__main__':
    main()
   
