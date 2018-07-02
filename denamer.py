#!/usr/bin/env python

import os
import readline
import pdb

print
directory= raw_input('Please enter directory for images: ').strip()
ImageIDs = raw_input('Please enter Image IDs in a comma-separated list: ').split(',')

ext=['s','u']
tifs=[]
jpgs=[]

for filename in os.listdir(directory):
    if '.tif' in filename:
        tifs.append(filename)
    elif '.jpg' in filename:
        jpgs.append(filename)
    else: 
        print "%s not a jpg or tif" % (filename) 

correctly_denamed = 0
not_found = 0
not_found_list = []

for x in range(len(ImageIDs)):
    if len(tifs)>0:
        for i in ext:
            capture_seq = str(x+1) + str(i)+'.tif'
            image_id = str(ImageIDs[x].strip()) + str(i)+'.tif'
            if os.path.exists(directory+'/'+image_id):
                os.rename(directory+'/'+image_id, directory+'/'+capture_seq)
                print image_id + " renamed correctly to " + capture_seq
                correctly_denamed = correctly_denamed + 1
            elif os.path.exists(directory+'/'+capture_seq):
                print "%s already renamed" % (capture_seq)
            else:
                not_found = not_found + 1
                not_found_list.append(image_id)
                print image_id + " not found in folder"
    else:
        pass
    if len(jpgs)>0:
        capture_seq = str(x+1) +'.jpg'
        image_id = str(ImageIDs[x].strip()) +'.jpg'
        if os.path.exists(directory+'/'+image_id):
            os.rename(directory+'/'+image_id, directory+'/'+capture_seq)
            print image_id + " renamed correctly to " + capture_seq
        elif os.path.exists(directory+'/'+capture_seq):
            print "%s already renamed" % (capture_seq)
        else:
            print image_id + " not found in folder"
    else:
        pass

print
print 
print
print "Denamer report: "
print
print str(correctly_denamed) + " images correctly denamed"
if not_found > 0:
    print str(not_found) + " images not found in folder: "
print
if not_found_list:
    ANSWER = raw_input("Would you like to see the list of images not found in your folder? Y or N? ")
    if ANSWER == "Y" or ANSWER == "y":
        print "Images not found include the following: "
        for i in not_found_list:
            print i
    else: 
        exit