#!/usr/bin/env python
import os
import sys
import shutil
import subprocess
from PIL import Image
import multiprocessing
from joblib import Parallel, delayed
import tqdm

current_path = os.getcwd()
size = 3500, 3500

def main():


    for root, dirs, files in os.walk(current_path, topdown=False):
        for name in files:
            print(os.path.join(root, name))
            if os.path.splitext(os.path.join(root, name))[1].lower() == ".tif":
                outputfile = os.path.splitext(os.path.join(root, name))[0] + ".jpg"

                im = Image.open(os.path.join(root, name))
                im.thumbnail(size,Image.ANTIALIAS)
                im.save(outputfile, "JPEG", quality=80)


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
