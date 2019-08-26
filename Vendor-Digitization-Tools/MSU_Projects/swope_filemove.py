#!/usr/bin/env python

## will pull out all files in a text file.
## currently, files need to be seperated by a new line. Can be changed to make them comma seperated or anything you'd like probably

import subprocess

file_list = input("\nDrag the list of files you'd like to move here:\n")
file_list = file_list.replace("\\","")
file_list = file_list.rstrip()
out_dir = input("\nDrag the folder containing the files you'd like to move here:\n")
out_dir = out_dir.replace("\\","")
out_dir = out_dir.rstrip()
in_dir = input("\nDrag the folder you're moving the files to here:\n")
in_dir = in_dir.replace("\\","")
in_dir = in_dir.rstrip()


f = open(file_list, "r")
lines = [line.rstrip("\n") for line in f.readlines()]

for line in lines:
    out_file = out_dir + "/" + line
    subprocess.call("rsync -ratvhP " + str(out_file) + " " + str(in_dir), shell=True)
