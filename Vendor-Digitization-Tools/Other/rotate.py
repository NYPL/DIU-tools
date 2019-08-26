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
dir = [i for i in os.listdir(current_path) if i.endswith('tif')]

print("How would you like the ODD numbered files to be rotated? CW or CCW?\n\n")
rotation = input()


if rotation == 'CW':
    for file in dir:
        ## stripping off everything but the file number
        number = int(file[-10:-6])
        ## must be in this format:
        ## INFOINFOINFO_####_u.tif
        ## i.e. have a four digit image counter, with an underscore, letter, file extension
        ## seeing if number is even or odd, rotating accordingly
        if number % 2 == 0:
            print("\nRotating " + file + " CCW")
            subprocess.call('mogrify -rotate "-90" -type TrueColor ' + str(file), shell=True)

        else:
            print("\nRotating " + file + " CW")
            subprocess.call('mogrify -rotate "90" -type TrueColor ' + str(file), shell=True)

## repeating above with different captialization
if rotation == 'cw':
    for file in dir:
        number = int(file[-10:-6])
        if number % 2 == 0:
            print("\nRotating " + file + " CCW")
            subprocess.call('mogrify -rotate "-90" -type TrueColor ' + str(file), shell=True)

        else:
            print("\nRotating " + file + " CW")
            subprocess.call('mogrify -rotate "90" -type TrueColor ' + str(file), shell=True)

## for if you want odd to go CCW
if rotation == 'CCW':
    for file in dir:
        number = int(file[-10:-6])
        if number % 2 == 0:
            print("\nRotating " + file + " CW")
            subprocess.call('mogrify -rotate "90" -type TrueColor ' + str(file), shell=True)

        else:
            print("\nRotating " + file + " CCW")
            subprocess.call('mogrify -rotate "-90" -type TrueColor ' + str(file), shell=True)

if rotation == 'ccw':
    for file in dir:
        number = int(file[-10:-6])
        if number % 2 == 0:
            print("\nRotating " + file + " CW")
            subprocess.call('mogrify -rotate "90" -type TrueColor ' + str(file), shell=True)

        else:
            print("\nRotating " + file + " CCW")
            subprocess.call('mogrify -rotate "-90" -type TrueColor ' + str(file), shell=True)
