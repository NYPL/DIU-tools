#!/usr/bin/env python

import os
import subprocess
import sys


## moves all tif files in a directory structure w/o copying over the actual directories. Essentially moves while also flattening. Probably an easier way to do this but I could not get --exclude or --include for rysnc to work.
## will work with any level of depth

## to use, type the following into termina:
## python3 /Path/To/Directory/To/Move/And/Flatten /Path/To/Destination/Directory


# print("Enter the directory you'd like to move and flatten.\n")
# origin_folder = input()
origin_folder = str(sys.argv[1])
origin_folder = origin_folder.replace('\\', '')
origin_folder = origin_folder.rstrip()

# print("Enter the destination directory.\n")
# dest_folder = input()
dest_folder = str(sys.argv[2])
dest_folder = dest_folder.replace('\\', '')
dest_folder = dest_folder.rstrip()


for root, directories, filenames in os.walk(origin_folder):
    print(root)
    for filename in filenames:
        if os.path.splitext(os.path.join(root,filename))[1].lower() == ".tif":
            move_file = os.path.join(root, filename)
            subprocess.call('rsync -ratvhP ' + str(move_file) + ' ' + str(dest_folder), shell=True)
