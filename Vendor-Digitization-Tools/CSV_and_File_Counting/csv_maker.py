#!/usr/bin/env python

## Goes through however many folders you'd like taking inventory of them. Will loop through until you tell it to stop. ##

## Currently works w/ this folder structure/naming convention: ##
## Volume###_YYYYMMDD_YYYYMMDD ## <-- this can be anything
## - Volume## <-- must be 'Volume' number followed by number
##   - Issue### <-- must be 'Issue' followed by number
##     - YYYYMMDD <-- must be the date in this formatting
## if folder structure is different contact me! (katiewolf@nypl.org) I can rewrite!


import os
import csv
import glob
import re
from time import sleep

## change the field names you need here! ##
fieldnames = ['item_number', 'parent_uuid', 'originInfo_datetype', 'originInfo_datesingleyear', 'originInfo_datesinglemonth', 'originInfo_datesingleday', 'titleInfo_partnumber', 'titleInfo_title', 'cap_num']

## for item number count ##
## note! this doesn't sort by date yet, so these might be a bit useless ##
item_number = 1

## Enter the filename you'd like here ##
filename = input('\n\n--------\nWhat would you like to name this file? The format is already set as CSV!\n--------\n\n') + '.csv'

print('\n\n--------\nOkay! Making ' + filename + ' for you!\n--------\n\n')

f = open(filename, 'w')
w = csv.DictWriter(f, fieldnames=fieldnames)
w.writeheader()

# ## Changes the titleInfo_title input ##
# print("\n\n---------\nWhat is the title of the collection you're working with?\n---------\n\n")
# title_info = input()
#
# print('\n\n---------\nAlright! This collection is called ' + title_info + '.\n---------\n\n')
title_info = 'The Reform advocate'

## The first directory being added to the CSV ##
print("\n\n--------\nDrag over the directory you'd like to make a CSV for.\n--------\n\n")
folder = input()
current_path = folder.replace('\\', '')
current_path = current_path.rstrip()

print(f'\n\n--------\nAlright! The directory is {current_path}!\n--------\n\n')

print('\n\n--------\nEnter the UUID for this directory.\n--------\n\n')
uuid = input()

print(f'\n\n--------\nAlright! The UUID is {uuid}!\n--------\n\n')

print('\n\n---------\nStarting inventory . . . \n---------\n')

sleep(1)

## Starts the dig into the folders! ##
for dir in os.scandir(current_path):
    if dir.is_dir():
        ## isolating the directory name from the entire directory path ##
        dir_l1 = os.path.basename(dir)
        ## striping off Volume and leading zeros for consistent formatting ##
        vol_num = (dir_l1[6:]).lstrip('0')
        for subdir_1 in os.scandir(dir.path):
            if subdir_1.is_dir():
                dir_l2 = os.path.basename(subdir_1)
                issue_num = (dir_l2[5:]).lstrip('0')
                for subdir_2 in os.scandir(subdir_1.path):
                    if subdir_2.is_dir():
                        dir_l3 = os.path.basename(subdir_2)
                        year = dir_l3[0:4]
                        month = dir_l3[4:6]
                        day = dir_l3[6:]

                        # counting both TIF and tif files
                        for root, dirs, files in os.walk(subdir_2):
                            fc_lc = len(glob.glob1(subdir_2, '*.tif'))
                            fc_caps = len(glob.glob1(subdir_2, '*.TIF'))
                            filecount = fc_lc + fc_caps

                        # crafting part number for CSV
                        partnumber = 'Vol. ' + vol_num + ', no. ' + issue_num

                        print('Item Number: ', item_number, '\n', 'Year: ', year, '\n', 'Month: ', month, '\n', 'Day: ', day, '\n', partnumber, '\n', 'Filecount:', filecount, '\n')

                        # writing info out to CSV
                        w.writerow({'item_number': item_number,'parent_uuid': uuid, 'originInfo_datetype': 'dateIssued', 'originInfo_datesingleyear': year, 'originInfo_datesinglemonth': month, 'originInfo_datesingleday': day, 'titleInfo_partnumber': partnumber, 'titleInfo_title': title_info, 'cap_num': filecount})

                        ## adding up the item numbers! ##
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
        path = folder.replace('\\', '')
        path = path.rstrip()

        print(f'\n\n--------\nAlright! The directory is {path}!\n--------\n\n')

        print(f'\n\n--------\nEnter the UUID for this directory.\n--------\n\n')
        new_uuid = input()

        print(f'\n\n--------\nAlright! The UUID is {new_uuid}!\n--------\n\n')

        sleep(1)

        for dir in os.scandir(path):
            if dir.is_dir():
                dir_l1 = os.path.basename(dir)
                vol_num = (dir_l1[6:]).lstrip('0')
                for subdir_1 in os.scandir(dir.path):
                    if subdir_1.is_dir():
                        dir_l2 = os.path.basename(subdir_1)
                        issue_num = (dir_l2[5:]).lstrip('0')
                        for subdir_2 in os.scandir(subdir_1.path):
                            if subdir_2.is_dir():
                                dir_l3 = os.path.basename(subdir_2)
                                year = dir_l3[0:4]
                                month = dir_l3[4:6]
                                day = dir_l3[6:]

                                for root, dirs, files in os.walk(subdir_2):
                                    fc_lc = len(glob.glob1(subdir_2, '*.tif'))
                                    fc_caps = len(glob.glob1(subdir_2, '*.TIF'))
                                    filecount = fc_lc + fc_caps

                                partnumber = 'Vol. ' + vol_num + ', no. ' + issue_num

                                print('Item Number: ', item_number, '\n', 'Year: ', year, '\n', 'Month: ', month, '\n', 'Day: ', day, '\n', partnumber, '\n', 'filecount', filecount, '\n')

                                w.writerow({'item_number': item_number, 'parent_uuid': new_uuid, 'originInfo_datetype': 'dateIssued', 'originInfo_datesingleyear': year, 'originInfo_datesinglemonth': month, 'originInfo_datesingleday': day, 'titleInfo_partnumber': partnumber, 'titleInfo_title': title_info, 'cap_num': filecount})

                                item_number = item_number + 1
        f.close()

    if go_again == 'N' or go_again == 'n':
        print('\n\n---------\nAlright! Bye!\n---------\n')
        f.close()
        break

f.close()
