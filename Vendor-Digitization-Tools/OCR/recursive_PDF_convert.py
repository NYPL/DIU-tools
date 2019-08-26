#!/usr/bin/env python3

import os
import subprocess
import sys

## converts TIFs to PDFs recursively

current_path = str(sys.argv[1])
current_path = current_path.replace('\\', '')
current_path = current_path.rstrip()


for directory in os.scandir(current_path):
    if directory.is_dir():
        dir_name = os.path.join(current_path, directory)
        if dir_name[-4:] != "done":
            for file in os.scandir(directory):
                pdf = os.path.join(current_path, file)
                if os.path.splitext(pdf)[1] == ".pdf":
                    if (pdf[-8:-4]) != "done":
                        tif = pdf[:-4] + "_%d.tif"
                        print("Converting " + pdf)
                        # subprocess.call("convert units PixelsPerInch -colorspace rgb -density 800 " + str(pdf) + " -resize 25% " + str(tif), shell=True)
                        subprocess.call("gs -q -dNOPAUSE -r800 -sDEVICE=tiff24nc -sOutputFile=" + str(tif) + " " + str(pdf) + " -c quit", shell=True)
                        new_file = pdf.replace(".pdf", "_done.pdf")
                        os.rename(pdf, new_file)
            new_dir = dir_name + "_done"
            os.rename(dir_name, new_dir)
            print("Done converting " + dir_name)

new_path = current_path + "_done"
os.rename(current_path, new_path)
print("Finished with " + current_path)

print('\a\a\a')
