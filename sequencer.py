#!/usr/bin/env python

import os
import readline
import re

print

directory= raw_input('Please enter directory for images: ').strip()

def get_alphanum_key_func():
    convert = lambda text: int(text) if text.isdigit() else text 
    return lambda s: [convert(c) for c in re.split('([0-9]+)', s)]

def natural_sort(list):
    sort_key = get_alphanum_key_func()
    list.sort(key=sort_key)

def check_ext():
    tifs=[]
    jpgs=[]
    for filename in os.listdir(directory):
        if '.tif' in filename:
            tifs.append(filename)
        elif '.jpg' in filename:
            jpgs.append(filename)
    if len(tifs) > 0 and ('u' not in x or 's' not in x for x in tifs):
        print
        print
        print("Your folder contains tifs, but your filenames do not contain 's' or 'u'. Exiting.")
    if len(jpgs) > 0 and ('u' not in x or 's' not in x for x in jpgs):
        print
        print
        print("Your folder contains jpgs, but your filenames do not contain 's' or 'u'. Exiting.")
    if len(tifs) > 0 and len(jpgs) > 0:
        print
        print
        print('Your folder contains jpgs and tifs. Cannot resequence. Exiting.')
        exit()
    else:
        pass

u_files = []
def make_u_list():
    for filename in os.listdir(directory):
        if 'u' in filename:
            u_files.append(filename)
    natural_sort(u_files)
    return u_files

s_files = []
def make_s_list():
    for filename in os.listdir(directory):
        if 's' in filename:
            s_files.append(filename)
    natural_sort(s_files)
    return s_files

def rename_files():
    s_renamed = 0
    u_renamed = 0
    new_u = 0
    new_s = 0
    print
    for u_file in make_u_list():
        old_u = re.split('([0-9]+)', u_file)[1]
        ext = re.split('([0-9]+)', u_file)[2]
        new_u = new_u + 1
        os.rename(directory + '/' + old_u + ext, directory + '/' + str(new_u) + ext)
        print(str(old_u) + ext + " resequenced to " + str(new_u) + ext)
        s_renamed = s_renamed + 1
    for s_file in make_s_list():
        old_s = re.split('([0-9]+)', s_file)[1]
        ext = re.split('([0-9]+)', s_file)[2]
        new_s = new_s + 1
        os.rename(directory + '/' + old_s + ext, directory + '/' + str(new_s) + ext)
        print(str(old_s) + ext + " resequenced to " + str(new_s) + ext)
        u_renamed = u_renamed + 1
    print
    print 
    print
    print "Sequencer report: "
    print
    print str(s_renamed + u_renamed) + " files resequenced"
    print

def main():
    check_ext()
    rename_files()

if __name__ == '__main__':
    main()
