#!/usr/bin/env python

from PIL import Image
import pytesseract
import re
import sys
import os
import subprocess
import cv2


current_path = str(sys.argv[1])
current_path = current_path.replace('\\', '')
current_path = current_path.rstrip()

# current_path = os.getcwd()

for file in os.scandir(current_path):
    file = os.path.join(current_path, file)
    if os.path.splitext(file)[1] == ".tif":
        # subprocess.call("./textcleaner.sh -e normalize -f 15 -o 2 -s 1 " + file + " temp.png", shell=True)
        # temp_file = current_path + "/temp.png"
        # img = Image.open(temp_file)
        print(file)

        image = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
        (thresh, bw_image) = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        crop_img = bw_image[230:6400, 20:4350]

        # im = cv2.imread(file, cv2.IMREAD_COLOR)
        # crop_img = im[230:6400, 20:4350]

        # image = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
        # crop_img = image[230:6400, 20:4350]

        # image = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
        # ret, thresh = cv2.threshold(image, 127, 255, cv2.THRESH_TRUNC)
        # crop_img = thresh[230:6400, 20:4350]

        # image = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
        # thresh, bw_image = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)
        # crop_img = bw_image[230:6400, 20:4350]
        #
        # image = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
        # ret, thresh = cv2.threshold(image, 250, 255, cv2.THRESH_TRUNC)
        # crop_img = thresh[230:6400, 20:4350]

        write_file = str(file) + "_1.png"
        cv2.imwrite(write_file, crop_img)

        temp_file = "{}.png".format(os.getpid())
        # cv2.imwrite(temp_file, bw_image)
        cv2.imwrite(temp_file, crop_img)

        config = ('-l eng --oem 1 --psm 3')
        img = Image.open(temp_file)
        text = pytesseract.image_to_string(img, config=config)

        out_file = re.sub(".tif", "_1.txt", file.split("\\")[-1])
        print(out_file)

        print("Done with " + file)

        text_file = open(out_file, "w")
        text_file.write(text)
        text_file.close()

        os.remove(temp_file)
