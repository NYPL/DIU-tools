#!/usr/bin/env python

import os
import csv
import re
import glob
from time import sleep


fieldnames = ['item_number', 'parent_uuid', 'originInfo_datetype', 'originInfo_datesingleyear', 'originInfo_datesinglemonth', 'originInfo_datesingleday', 'titleInfo_partnumber', 'titleInfo_title', 'cap_num']

## Enter the filename you'd like here ##
filename = input('\n\n--------\nWhat would you like to name this file? The format is already set as CSV!\n--------\n\n') + '.csv'

print('\n\n--------\nOkay! Making {filename} for you!\n--------\n\n')

f = open(filename, 'w')
w = csv.DictWriter(f, fieldnames=fieldnames)
w.writeheader()

## Changes the titleInfo_title input ##
# print("\n\n---------\nWhat is the title of the collection you're working with?\n---------\n\n")
# title_info = input()
title_info = "The Negro world"


print('\n\n---------\nAlright! This collection is called ' + title_info + '.\n---------\n\n')

## The first directory being added to the CSV ##
print("\n\n--------\nDrag over the directory you'd like to make a CSV for.\n--------\n\n")
folder = input()
current_path = folder.replace('\\', '')
current_path = current_path.rstrip()

print(f'\n\n--------\nAlright! The directory is {current_path}!\n--------\n\n')


## UUIDs not created yet ##
# print('\n\n--------\nEnter the UUID for this directory.\n--------\n\n')
# uuid = input()
#
# print(f'\n\n--------\nAlright! The UUID is {uuid}!\n--------\n\n')
#
print('\n\n---------\nStarting inventory . . . \n---------\n')

sleep(1)


## for item number count ##
## note! this doesn't sort by date, so these might be a bit useless ##
item_number = 1

vol_num = os.path.basename(current_path)[7:]
vol_num = vol_num.lstrip("0")

for dir in os.scandir(current_path):
    if dir.is_dir():
        vol_num = os.path.basename(current_path)[7:]
        vol_num = vol_num.lstrip("0")
        dir_name = os.path.basename(dir)
        print(dir_name)
        issue_num = (dir_name[3:5]).replace("_", "")
        year = dir_name[-4:]
        day = (dir_name[-7:-4]).replace("_", "")
        month = (dir_name[5:8]).replace("_", "")
        month = month.lstrip("0")

        part_num = 'Vol. ' + vol_num + ', no. ' + issue_num

        dir_path = os.path.normpath(dir)
        for root, dirs, files in os.walk(dir_path):
            filecount = len(glob.glob1(dir_path, '*.tif'))


        print(' Item Number: ', item_number, '\n', 'Year: ', year, '\n', 'Month: ', month, '\n', 'Day: ', day, '\n', part_num, '\n', 'Filecount:', filecount, '\n')


        # writing info out to CSV
        w.writerow({'item_number': item_number, 'originInfo_datetype': 'dateIssued', 'originInfo_datesingleyear': year, 'originInfo_datesinglemonth': month, 'originInfo_datesingleday': day, 'titleInfo_partnumber': part_num, 'titleInfo_title': title_info, 'cap_num': filecount})

        item_number = item_number + 1

f.close()


## starting up the loop! ##

while True:

    print('\n\n---------\nWould you like add another directory to this CSV?\n---------\nY or N?\n---------\n\n')
    go_again = input()


    if go_again == 'Y' or go_again == 'y':

        f = open(filename, 'a')
        w = csv.DictWriter(f, fieldnames=fieldnames)

        print("\n\n--------\nDrag over the directory you'd like to inventory.\n--------\n\n")
        folder = input()
        current_path = folder.replace('\\', '')
        current_path = current_path.rstrip()

        print(f'\n\n--------\nAlright! The directory is {current_path}!\n--------\n\n')

        # print(f'\n\n--------\nEnter the UUID for this directory.\n--------\n\n')
        # new_uuid = input()
        #
        # print(f'\n\n--------\nAlright! The UUID is {new_uuid}!\n--------\n\n')

        sleep(1)

        for dir in os.scandir(current_path):
            if dir.is_dir():
                vol_num = os.path.basename(current_path)[7:]
                vol_num = vol_num.lstrip("0")
                dir_name = os.path.basename(dir)
                print(dir_name)
                issue_num = (dir_name[3:5]).replace("_", "")
                year = dir_name[-4:]
                day = (dir_name[-7:-4]).replace("_", "")
                month = (dir_name[5:8]).replace("_", "")
                month = month.lstrip("0")

                part_num = 'Vol. ' + vol_num + ', no. ' + issue_num

                dir_path = os.path.normpath(dir)
                for root, dirs, files in os.walk(dir_path):
                    filecount = len(glob.glob1(dir_path, '*.tif'))


                print(' Item Number: ', item_number, '\n', 'Year: ', year, '\n', 'Month: ', month, '\n', 'Day: ', day, '\n', part_num, '\n', 'Filecount:', filecount, '\n')


                # writing info out to CSV
                w.writerow({'item_number': item_number, 'originInfo_datetype': 'dateIssued', 'originInfo_datesingleyear': year, 'originInfo_datesinglemonth': month, 'originInfo_datesingleday': day, 'titleInfo_partnumber': part_num, 'titleInfo_title': title_info, 'cap_num': filecount})

                item_number = item_number + 1

        f.close()

    if go_again == 'N' or go_again == 'n':
        print('\n\n---------\nAlright! Bye!\n---------\n')
        f.close()
        break

f.close()
