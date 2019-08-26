#!/usr/bin/env python

import os
import readline
import pdb

directory= raw_input('\nPlease enter directory for images: ').strip()
ImageIDs = raw_input('\nPlease enter Image IDs in a comma-separated list: ').split(',')

tifs=[]
jpgs=[]

for filename in os.listdir(directory):
    if '.tif' in filename:
        tifs.append(filename)
    elif '.jpg' in filename:
        jpgs.append(filename)
    else:
        print "%s not a jpg or tif" % (filename)

correctly_renamed = 0
not_found = 0
not_found_list = []

for x in range(len(ImageIDs)):
    if len(tifs)>0:
        for i in tifs:
            capture_seq = str(x+1) + str(i)+'.tif'
            image_id = str(ImageIDs[x].strip()) + str(i)+'.tif'
            if os.path.exists(directory+'/'+capture_seq):
                os.rename(directory+'/'+capture_seq, directory+'/'+image_id)
                print capture_seq + " renamed correctly to " + image_id
                correctly_renamed = correctly_renamed + 1
            elif os.path.exists(directory+'/'+image_id):
                print "%s already renamed" % (image_id)
            else:
                not_found = not_found + 1
                not_found_list.append(capture_seq)
                print capture_seq + " not found in folder"
    else:
        pass
    if len(jpgs)>0:
        capture_seq = str(x+1) +'.jpg'
        image_id = str(ImageIDs[x].strip()) +'.jpg'
        if os.path.exists(directory+'/'+capture_seq):
            os.rename(directory+'/'+capture_seq, directory+'/'+image_id)
            print capture_seq + " renamed correctly to " + image_id
        elif os.path.exists(directory+'/'+image_id):
            print "%s already renamed" % (image_id)
        else:
            print capture_seq + " not found in folder"
    else:
        pass

print
print
print
print "Renamer report: "
print
print str(correctly_renamed) + " images correctly renamed"
if not_found > 0:
    print str(not_found) + " images not found in folder: "
print
if not_found_list:
    ANSWER = raw_input("Would you like to see a list of images not found in your folder? Y or N? ")
    if ANSWER == "Y" or ANSWER == "y":
        print "Images not found include the following: "
        for i in not_found_list:
            print i
    else:
        exit
