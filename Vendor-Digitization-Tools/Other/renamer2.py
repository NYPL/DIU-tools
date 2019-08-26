#!/usr/bin/env python3

import os
import readline
import pdb


directory = input("Please enter directory with images: ").strip()
file_names = input("Please enter Image ID list: ").split(',')

print(directory)

tifs = []
jpgs = []

for filename in os.listdir(directory):
    if '.tif' in filename:
        tifs.append(filename)
    elif '.jpg' in filename:
        jpgs.append(filename)
    else:
        print(f"{filename} is not a JPG or a TIF, sorry!")

with open(filenames) as list:
    filedata = filenames.read().split(',')
    os.rename()

print(tifs)
print(jpgs)
