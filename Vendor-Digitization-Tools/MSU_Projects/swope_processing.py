#!/usr/bin/env python

## This script is an automated version of the process done for the Swopes project ##
## It takes up to three inputs:
##          - a TXT file of all the swopes files that need to be found (required)
##          - An "in" directory where you'd like the files in the list to be moved to (required)
##          - An "out" directory where you'd like to search for the files (currently using to the ICE Swope Drive All folder)

## To run the script, have a .TXT file with all the swope IDs you'd like to look for, separated by a new line. If you'd like them to be comma separated, that can be changed in the ##READING THE FILE## section of the script.


## Importing required libraries ##
import os
import subprocess

# Drag over the .TXT file containing all the swope IDs ##

file_list = input("\nDrag the list of files you'd like to move here:\n")
file_list = file_list.replace("\\","")
file_list = file_list.rstrip()

## Drag over the place where you'd like to search for files. This WILL search through multiple layers of folders ##

out_dir = input("\nDrag the folder containing the files you'd like to move here:\n")
out_dir = out_dir.replace("\\","")
out_dir = out_dir.rstrip()


## Drag over the folder where you'd like the files to end up ##

in_dir = input("\nDrag the folder you're moving the files to here:\n")
in_dir = in_dir.replace("\\","")
in_dir = in_dir.rstrip()


## READING THE FILES ##
## Opening up the .TXT file and renaming the files to match the format found in the Swope Drive ##

f = open(file_list, "r")
lines = [line.rstrip("\n") for line in f.readlines()]

## Empyt list where renamed files will go to be used later ##
out_files = []

## RENAMING THE FILES ##
print("Renaming the files to match the output file format!\n")
for line in lines:
    line = line.replace("swope_", "")
    line = line.zfill(8)
    out_file = line + ".jpg"
    out_files.append(out_file)
    print(out_file)

## REMOVING DUPLICATES ##
## Looking for duplicates and potentially removing them #
print("Looking for duplicates...")
seen = {}
dupes = []
for x in out_files:
    if x not in seen:
        seen[x] = 1
    else:
        if seen[x] ==1:
            dupes.append(x)
        seen[x] +=1

dupe_file = open(in_dir + "/duplicate_files.txt", "w")
if len(dupes) == 0:
    print("\nThere were no duplicates in this batch!")
else:
    print("\nThe following items were duplicates: ")
    for file in dupes:
        print("\n" + file)
        ## Making a .TXT file listing the duplicates
        dupe_file.write(file)

    print("\nWould you like to remove the duplicates from the list? Y or N?")
    dupe_answer = input()
    ## removing duplicates if required
    if dupe_answer == "Y" or dupe_answer == "y":
        out_files = list(dict.fromkeys(out_files))
        print("\nAlright, duplicates removed! A .TXT file has been made listing the duplicates.")
    else:
        print("\nOkay! Nothing changed! A .TXT file has been made listing the duplicates.")

f.close()
dupe_file.close()

## LOOKING FOR FILES ##
print("\n~~~~~~~~~~\n")
print("Looking for files in the Swope Drive.")

found_files = []
moving_files = []
for dirpath, dirnames, files in os.walk(out_dir):
    for name in files:
        if name in out_files:
            found_files.append(name)
            print(name)
            full_name = os.path.join(dirpath, name)
            moving_files.append(full_name)

## FINDING THE MISSING FILES ##

missing_file = open(in_dir+"/missing_files.txt", "w")

difference= (set(out_files).difference(found_files))
if len(difference) == 0:
    print("All files found!")
else:
    print("The following items weren't found: ")
    for item in difference:
        print(item + "\n")
        ## Making a .TXT file listing all the differences ##
        missing_file.write(item)

## MOVING THE FILES ##
print("Okay! Moving all found items to the in directory!\n\n")
for file in moving_files:
        subprocess.call("rsync -ratvhP " + str(file) + " " + str(in_dir), shell=True)

## REFORMATTING THE FILES ##
print("\nConverting files to TIFs.")
for file in os.scandir(in_dir):
    jpg = os.path.join(in_dir, file)
    if jpg[-4:] == ".jpg":
        subprocess.call("mogrify -format tif " + jpg, shell=True)
        subprocess.call("rm -rf " + jpg, shell=True)

## RE-RENAMING THE FILES ##
print("\nRenaming the files.")
for file in os.listdir(in_dir):
    if file[-4:] == ".tif":
        full_file = os.path.join(in_dir, file)
        new_name = in_dir+ "/swope_" + file.lstrip("0")
        new_name = new_name.replace(".tif", "s.tif")
        os.rename(full_file, new_name)

## COMPARING ORIGINAL LIST TO NEW FILES ##
print("\nChecking the make sure everything matches!")
new_files = []
for file in os.listdir(in_dir):
    if file[-4:] == ".tif":
        file = file[:-4]
        new_files.append(file)

file_check = (set(lines).difference(new_files))
if len(file_check) == 0:
    print("\nThe lists match!")
else:
    print("\nOh no! There's a difference! Here's the difference: ")
    for item in file_check:
        print(item + "\n")


# GIVING A SUMMARY ##
in_count = len(lines)
duplicates_count = len(dupes)
moved_count = len(moving_files)
missing_count = len(difference)
print("\n~~~~~~\nSession summary: \nInput count: " + str(in_count) + "\nDuplicate count: " + str(duplicates_count) + "\nMoved count: " + str(moved_count) + "\nMissing count: " + str(missing_count) + "\n~~~~~~")
