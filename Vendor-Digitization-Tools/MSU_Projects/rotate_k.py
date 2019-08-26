#!/usr/bin/env python

import os
import subprocess
import re


## for rotating odd and even numbered tifs in different directions
## allows user to input which direction each tif should go
## Just drag over directory that needs rotation and say whether odd should go CCW or CW. It will automatically rotate even the other direction

print("Enter the directory you'd like to rotate.\n")
folder = input()
current_path = folder.replace('\\', '')
current_path = current_path.rstrip()
os.chdir(current_path)

print ("\nAlright, rotating files in " + current_path + '\n')
dir = [i for i in os.listdir(current_path) if i.endswith('JPG')]

print("How would you like the ODD numbered files to be rotated? CW or CCW?\n\n")
rotation = input()

if rotation == 'CW' or rotation == 'cw':
    for file in dir:
        number = int(file[0:6])
        print(number)
        if number % 2 == 0:
            print("\nRotating " + file + " CCW")
            subprocess.call('mogrify -rotate "-90" -type TrueColor ' + str(file), shell=True)

        else:
            print("\nRotating " + file + " CW")
            subprocess.call('mogrify -rotate "90" -type TrueColor ' + str(file), shell=True)

if rotation == 'CCW' or rotation == 'ccw':
    for file in dir:
        number = int(file[0:6])
        if number % 2 == 0:
            print("\nRotating " + file + " CW")
            subprocess.call('mogrify -rotate "90" -type TrueColor ' + str(file), shell=True)

        else:
            print("\nRotating " + file + " CCW")
            subprocess.call('mogrify -rotate "-90" -type TrueColor ' + str(file), shell=True)
