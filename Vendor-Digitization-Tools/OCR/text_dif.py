#!/usr/bin/env python3

import os
import pandas as pnd
import difflib

correct_path = input("<><><><>\nPlease drag over the folder containing the corrected OCR .txt files.\n")
correct_path = correct_path.replace("\\", "")
correct_path = correct_path.rstrip()

compare_path = input("<><><><>\nPlease drag over the folder containing the comparison OCR .txt files.\n")
compare_path = compare_path.replace("\\", "")
compare_path = compare_path.rstrip()

y_n = input("<><><><>\nWould you like to save the output CSV in your current working directory? Y or N \n")
if y_n == "Y" or y_n == "y":
    dest_path = os.getcwd()
if y_n == "N" or y_n == "n":
    dest_path = input("<><><><>\nWhere would you like to save the file?\n")
    dest_path = dest_path.replace("\\", "")
    dest_path = dest_path.rstrip()

data = []

for file in os.listdir(correct_path):
    if file[-4:] == ".txt":
        corr_file = correct_path + "/" + file
        comp_file = compare_path + "/" + file
        t1 = open(corr_file).readlines()
        t2 = open(comp_file).readlines()
        m = difflib.SequenceMatcher(None, t1, t2)
        ratio = m.ratio()
        file_num = [file, ratio]
        data.append(file_num)
        print("<><><><>\nDone comparing " + file + "")
df = pnd.DataFrame(data, columns=["file", "difflib_ratio"])

average = df["difflib_ratio"].mean()
print("\n<><><><>\nThe mean value of the difflib_ratio for this comparison is: " + str(average) + ".")

one_count = df.query("difflib_ratio == 1.000000").difflib_ratio.value_counts()
for value in one_count:
    print("\nThe number of ratios that equal 1 is: " + str(value) + ".")

zero_count = df.query("difflib_ratio == 0.000000").difflib_ratio.value_counts()
for value in zero_count:
    print("\nThe number of ratios that equal 0 is: " + str(value) + ".")


dest_csv = dest_path + "/difflib_ratios.csv"

df.to_csv(dest_csv, encoding="utf-8")
