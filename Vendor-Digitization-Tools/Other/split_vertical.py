#!/usr/bin/env python3

import os
import subprocess
import sys
import glob
from shutil import copyfile

current_path = str(sys.argv[1])
current_path = current_path.replace('\\', '')
current_path = current_path.rstrip()

## OPTION 1 ##
## recursive path for going through many folders

# for directory in os.scandir(current_path):
#     tif_list = []
#     if directory.is_dir():
#         print("\n\n<>-----<><>-----<><>-----<>\n\nWorking in " + str(os.path.normpath(directory)) + ". \n\n<>-----<><>-----<><>-----<>")
#         count = len(glob.glob1(directory, "*.tif"))
#         loop_range = list(range(2, count))
#         loop_range = [str(item) for item in loop_range]
#         for file in os.scandir(directory):
#             if os.path.splitext(file)[1] == ".tif":
#                 tif_path = os.path.normpath(file)
#                 tif_list.append(tif_path)
#         for tif in tif_list:
#             tif_num = tif[-5:-4]
#             tif_name = os.path.basename(tif)
#             if tif_num in loop_range:
#                 new_name_a = tif[:-4] + "-a.tif"
#                 new_name_b = tif[:-4] + "-b.tif"
#
#                 print("\n~ Converting " + tif_name +"! ~\n")
#                 subprocess.call("convert " + str(tif) + " -gravity West -crop 50%x100% +repage " + str(new_name_a), shell=True)
#                 subprocess.call("convert " + str(tif) + " -gravity East -crop 50%x100% +repage " + str(new_name_b), shell=True)
#
#             else:
#                 print("\n~ " + tif_name + " not in range. ~\n")
#         print("\n\n<>-----<><>-----<><>-----<>\n\nFinished with " + os.path.normpath(directory) + "!\n\n<>-----<><>-----<><>-----<>\n\n")
#         tif_list.clear()
#
# print("\n\n<>~~~~~<><>~~~~~<><>~~~~~<>\n\nFinished with " + current_path + "!\n\n<>~~~~~<><>~~~~~<><>~~~~~<>>\n\n")

## OPTION 2 ##
## non-recursive; splits all files in a folder

current_path = str(sys.argv[1])
current_path = current_path.replace('\\', '')
current_path = current_path.rstrip()


print("\n\n<>-----<><>-----<><>-----<>\n\nWorking in " + str(os.path.normpath(current_path)) + ". \n\n<>-----<><>-----<><>-----<>")
tif_list = []

for file in os.scandir(current_path):
    if os.path.splitext(file)[1] == ".tif":
            tif_path = os.path.normpath(file)
            tif_list.append(tif_path)

for tif in tif_list:
    tif_name = os.path.basename(tif)
    new_name_a = tif[:-4] + "-a.tif"
    new_name_b = tif[:-4] + "-b.tif"


    print("\n~ Converting " + tif_name +"! ~\n")
    
    subprocess.call("convert " + str(tif) + " -gravity West -crop 50%x100% +repage " + str(new_name_a), shell=True)
    subprocess.call("convert " + str(tif) + " -gravity East -crop 50%x100% +repage " + str(new_name_b), shell=True)

tif_list.clear()

print("\n\n<>~~~~~<><>~~~~~<><>~~~~~<>\n\nFinished with " + current_path + "!\n\n<>~~~~~<><>~~~~~<><>~~~~~<>>\n\n")
