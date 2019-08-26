#!/usr/bin/env python
import os
import sys
import shutil
import subprocess

#image editting
from PIL import Image

# parallel stuff
import multiprocessing
from joblib import Parallel, delayed

## this script will convert your TIFS to lower quality/sized JPGs for quicker QC. It will also make a folder and move all the JPGs to that folder##

current_path = os.getcwd()
size = 3500, 3500



p3 = "find . -name '*.tif' | parallel convert -format jpg -resize 3500x3500 {} {.}.jpg"

pro = subprocess.call(p3, stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)

def main():


    for child in os.scandir(current_path):
        if child.is_dir():
            for grandchild in os.scandir(child.path):
                if grandchild.is_dir():
                    newpath = os.path.join(grandchild.path, 'QC')
                    os.mkdir(newpath)

    for child in os.scandir(current_path):
        if child.is_dir():
            for grandchild in os.scandir(child.path):
                if grandchild.is_dir():
                    for file in os.listdir(grandchild):
                        if file.endswith('.jpg'):
                            sourcepath = os.path.join(grandchild, file)
                            newpath = os.path.join(grandchild, 'QC')
                            shutil.move(sourcepath, os.path.join(newpath, file))


if __name__ == '__main__': main()
