#!/usr/bin/env python3
## list folder names and number of files in them in csv/excel sheet
## section 1 will list directory, subdirectory, file filecount - for most file structures, including Brown Brothers
## section 2 will list directory, subdirectory 1, subdirectory 2, filecount - mostly used for City Record File Structure
## section 3 will list the directory, subdirectory 1, subdirectory 2, subdirectory 3, filecount - mostly used for Reform Advocate
## you just have to remove the #s from whichever section best suits your needs

import os
import csv
import glob
import re

# dir_list = next(os.walk('.'))[1]
# current_path = os.getcwd()
# ##name of top folder (won't be included in the spreadsheet)
# current_path = "/Volumes/Untitled 1/Brown Brothers/Raw - Tagged"

print("Enter the directory you'd like to inventory.")
folder = input()
current_path = folder.replace('\\', '')
current_path = current_path.rstrip()
print(current_path)

print("How many levels are there in the folder structure? (Do not include top level directory in count)")
levels = input()

print("What file extension are you counting? (Example options: tif, TIF, jpg, jpeg)")
ext = '*.' + input()

#####
## SECTION 1 ##
## MAIN FOLDER (will not be included in spreadsheet, should be same as the current_path)
##      - VOLUME FOLDER
##          - ISSUE Folder (w/ file count)
#####

if levels == '2':
    fieldnames = ['topdir', 'subdir', 'filecount']

    f = open('filecount.csv', 'w')
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()


    for dir in os.scandir(current_path):
        if dir.is_dir():
            topdir = (os.path.basename(dir))
            print(topdir)
            for subdir in os.scandir(dir.path):
                if subdir.is_dir():
                    foldname = (os.path.basename(subdir))
                    print(foldname)

                    for root, dirs, files in os.walk(subdir):
                        filecount = len(glob.glob1(subdir, ext))
                        print(filecount)


                    w.writerow({'topdir':topdir, 'subdir': foldname, 'filecount': filecount})
    f.close()


#####
## SECTION 2 ##
## MAIN FOLDER (current_path, won't be included in spreadsheet)
##      - COLLECTION FOLDER
##          - VOLUME FOLDER
##              - ISSUE FOLDER
######

elif levels == '3':
    fieldnames = ['topdir', 'subdir_one', 'subdir_two', 'filecount']

    f = open('filecount.csv', 'w')
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()


    for dir in os.scandir(current_path):
        if dir.is_dir():
            topdir = (os.path.basename(dir))
            print(topdir)
            for subdir in os.scandir(dir.path):
                if subdir.is_dir():
                    subdir_one = (os.path.basename(subdir))
                    print(subdir_one)
                    for grandchild in os.scandir(subdir.path):
                        if grandchild.is_dir():
                            subdir_two = (os.path.basename(grandchild))
                            print(subdir_two)

                            for root, dirs, files in os.walk(grandchild):
                                filecount = len(glob.glob1(grandchild, ext))
                                print(filecount)

                            w.writerow({'topdir':topdir, 'subdir_one': subdir_one, 'subdir_two':subdir_two, 'filecount': filecount})

    f.close()

#####
## SECTION 3 ##
## MADE FOR REFORM ADVOCATE FOLDER STRUCTURE ##
## MAIN FOLDER (current_path, won't be included in spreadsheet)
##      -VOLUME - DATE FOLDER
##          - VOLUME FOLDER
##              - ISSUE NUMBER FOLDER
##                  - ISSUE DATE FOLDER
#

elif levels == '4':
    fieldnames = ['DATE_RANGE', 'VOLUME', 'ISSUE_NUMBER', 'ISSUE_DATE', 'filecount']

    f = open('filecount.csv', 'w')
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()


    for dir in os.scandir(current_path):
        if dir.is_dir():
            topdir = (os.path.basename(dir))
            print(topdir)
            for subdir in os.scandir(dir.path):
                if subdir.is_dir():
                    subdir_one = (os.path.basename(subdir))
                    print(subdir_one)
                    for grandchild in os.scandir(subdir.path):
                        if grandchild.is_dir():
                            subdir_two = (os.path.basename(grandchild))
                            print(subdir_two)
                            for grandgrandchild in os.scandir(grandchild.path):
                                if grandgrandchild.is_dir():
                                    subdir_three = (os.path.basename(grandgrandchild))
                                    print(subdir_three)

                                    for root, dirs, files in os.walk(grandgrandchild):
                                        filecount = len(glob.glob1(grandgrandchild, ext))
                                        print(filecount)

                                    w.writerow({'DATE_RANGE':topdir, 'VOLUME': subdir_one, 'ISSUE_NUMBER':subdir_two, 'ISSUE_DATE':subdir_three, 'filecount': filecount})
    f.close()

#

else:
    print("That structure hasn't been accounted for yet!")
