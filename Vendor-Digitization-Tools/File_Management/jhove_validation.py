#!/usr/bin/env python
import os
import subprocess
import xml.etree.ElementTree as ET
import csv


## for validating and checking if TIFFs are well-formed with JHOVE.

os.chdir("/Applications/JHOVE")
print("Enter the directory you'd like to check.\n")
folder = input()
current_path = folder.replace('\\', '')
current_path = current_path.rstrip()

print (f"\nAlright, checking files in {current_path}\n")
dir = [i for i in os.listdir(current_path) if i.endswith('tif')]


xml_file = open("/Users/diunt-02/Desktop/validation.xml", 'w')

print(f"Checking {current_path}!")
xml = subprocess.call(["./jhove -h audit " + str(current_path)], shell=True, stdout=xml_file)

print("Done checking!")



header = ("File", "Status")
with open('/Users/diunt-02/Desktop/validation.csv', 'w') as f:
    w = csv.DictWriter(f, fieldnames = header)
    w.writeheader()

    tree = ET.parse("/Users/diunt-02/Desktop/validation.xml")
    root = tree.getroot()

    for audit in root:
        for file in audit:
            filename = file.text
            status = file.get('status')
            print(filename, status)
            w.writerow({"File": filename, "Status": status})
