#!/bin/bash

# setup - install imagemagick, parallel
# citation prompt after parallel install
#Creates PDF from S Files by first converting to jpg

echo "
Please drag in your folder and press [Enter]: 
"
read DIRECTORY

cd $DIRECTORY

echo "
working...."

mkdir $DIRECTORY/QC

ls $DIRECTORY/*.tif | time parallel -j+0 --eta 'convert {}[0] -resize 3500x3500 -quality 100 {.}.jpg'

mv *.jpg $DIRECTORY/QC

echo "
Success! QC derivatives have been created in QC subfolder
"
