#!/usr/bin/env python3
## this will remove the last line from a text file. Useful for an OCR situation. 

import os

current_path = "/Volumes/ice/Katie/TheValueOfNothing/pages_ocr/test"

i = 1
for file in os.scandir(current_path):
    file = os.path.normpath(file)
    if os.path.splitext(file)[1] == ".txt":
        f = open(file, "r")
        lines = f.readlines()
        f.close()
        w = open(file, "w")
        w.writelines([item for item in lines[:-1]])
        w.close()
