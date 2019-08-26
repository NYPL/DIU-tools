#!/usr/bin/env python

import os
import csv


dir_list = next(os.walk('.'))[1]
fieldnames = ['item_number','originInfo_dates', 'year', 'month', 'day', 'titleInfo_Part', 'titleinfo_Title', 'capture_cropped', 'capture_uncropped']

filename = input('Please Enter Reel Number: ') + ".csv"


f = open(filename, 'w')
w = csv.DictWriter(f, fieldnames=fieldnames)
w.writeheader()

for dir in dir_list:
    if dir.endswith('uncropped'):
        year_num = float(dir[3:-14])
        month_num = float(dir[7:-12])
        day_num = float(dir[9:-10])

        for root, dirs, files in os.walk(dir):
            filecount = len(files)

        w.writerow({'year':year_num, 'month':month_num, 'day':day_num, 'capture_uncropped':filecount})

f.close()
