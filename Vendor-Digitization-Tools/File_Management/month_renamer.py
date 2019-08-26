#!/usr/bin/env python

## Script for renaming the City Record directory names to better fit into to current CSV creation requirements and general filenaming specs ##

import os
import csv
import re



## Whatever directory you want to work with ##
# print("\n\n--------\nDrag over the directory you'd like to make a CSV for.\n--------\n\n")
# folder = input()
# current_path = folder.replace('\\', '')
# current_path = current_path.rstrip()


## CROPPED RENAMER ##

current_path = "/Volumes/lts2/CityRecord_Dinah/CityRecord/Cropped"

## Setting up the regexes needed to find names ##
re_reel_num = re.compile("(R[0-9]{1,3})")
re_year = re.compile("_(19[0-9]{2})")
re_month = re.compile("[0-9]_([A-Za-z]{3,9})_")
re_start_date = re.compile("_([0-9]{1,2})-[0-9]{1,2}_19")
re_end_date = re.compile("-([0-9]{1,2})_19")
re_note = re.compile("[a-z]_([A-Za-z]+)_")




fieldnames = ["Old_File_Name", "New_File_Name"]

f = open("cityrecord_namecheck.csv", "w")
w = csv.DictWriter(f, fieldnames = fieldnames)

for directory in os.scandir(current_path):
    if directory.is_dir():
        directory = directory.path
        for subdir in os.scandir(directory):
            if subdir.is_dir():
                subdir = os.path.basename(subdir)

                reel_num = re.findall(re_reel_num, subdir)[0]
                year = re.findall(re_year, subdir)[0]

                month = re.findall(re_month, subdir)[0]
                if month == "January":
                    month = "01"
                if month == "February":
                    month = "02"
                if month == "March":
                    month = "03"
                if month == "April":
                    month = "04"
                if month == "May":
                    month = "05"
                if month == "June":
                    month = "06"
                if month == "July":
                    month = "07"
                if month == "August":
                    month = "08"
                if month == "September":
                    month = "09"
                if month == "October":
                    month = "10"
                if month == "November":
                    month = "11"
                if month == "December":
                    month = "12"



                start_date = re.findall(re_start_date, subdir)
                if len(start_date) == 0:
                    start_date = "N/A"
                else:
                    start_date = start_date[0]

                end_date = re.findall(re_end_date, subdir)
                if len(end_date) == 0:
                    end_date = "N/A"
                else:
                    end_date = end_date[0]

                range_start = year + "-" + month + "-" + start_date
                range_end = year + "-" + month + "-" + end_date

                note = re.findall(re_note, subdir)
                if len(note) == 0:
                    note = "N/A"
                    new_name = reel_num + "_" + range_start + "_" + range_end
                else:
                    note = note[0]
                    new_name = reel_num + "_" + year + "-" + month + "_" + note


                w.writerow({"Old_File_Name": subdir, "New_File_Name": new_name})


f.close()



## UNCROPPED RENAMER ##
