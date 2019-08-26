#!/usr/bin/env python

## Script for comparing city record holding ##

import os
import csv
import re


## change this as necessary to match the directory you'd like to work with ##
uncropped_path = "/Volumes/lts2/CityRecord_Dinah/CityRecord/Uncropped/1947"


## Setting up the regexes needed to find names ##
re_reel_num = re.compile("(R[0-9]{1,3})")
re_year = re.compile("(19[0-9]{2})")
re_month = re.compile("(January|February|March|April|May|June|July|August|September|October|November|December)")
re_start_date = re.compile("([0-9]{1,2})-[0-9]{1,2}")
re_end_date = re.compile("[0-9]{1,2}-([0-9]{1,2})")
re_note = re.compile("_(?!January|February|March|April|May|June|July|August|September|October|November|December)([A-Z][A-Za-z]+)")
re_range = re.compile("([0-9]{1,2}-[0-9]{1,2})")
re_singledate = re.compile("([0-9]{8})")


date_list = []

for directory in os.scandir(uncropped_path):
    if directory.is_dir():
        directory_path = directory.path
        for subdir in os.scandir(directory_path):
            if subdir.is_dir():
                subdir = os.path.basename(subdir)
                if len(subdir) != 21:
                    pass
                else:
                    date = re.findall(re_singledate, subdir)
                    if len(date) == 0:
                        pass
                    else:
                        date = date[0]
                        date_list.append(date)

        reel_num = re.findall(re_reel_num, directory_path)
        if len(reel_num) == 0:
            print(directory_path)
        else:
            reel_num = reel_num[0]

        year = re.findall(re_year, directory_path)
        if len(year) == 0:
            print(directory_path)
        else:
            year = year[0]

        month = re.findall(re_month, directory_path)
        if len(month) == 0:
            print(directory_path)
        else:
            month = month[0]




        note = re.findall(re_note, os.path.basename(directory))
        if len(note) == 0:
            note = "NA"
            if len(date_list) >= 1:
                date_list.sort()
                start = date_list[0]
                start_day = start[-2:]
                end = date_list[-1]
                end_day = end[-2:]
                range = start_day + "-" + end_day
                new_name = uncropped_path + "/" + reel_num + "_" + month + "_" + range + "_" + year
            else:
                new_name = uncropped_path + "/" + reel_num + "_" + month + "_" + note + "_" + year
        else:
            note = note[0]
            new_name = uncropped_path + "/" + reel_num + "_" + month + "_" + note + "_" + year



        print(directory_path)
        print(new_name)
        print("\n")
        os.rename(directory_path, new_name)

    date_list.clear()
