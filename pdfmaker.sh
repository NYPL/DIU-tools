#!/bin/bash

# setup - install imagemagick, parallel
# citation prompt after parallel install
#Creates PDF from S Files by first converting to jpg

echo "
Please drag in your folder and press [Enter]: 
"
read DIRECTORY

cd $DIRECTORY

foldername=${DIRECTORY##*/}

echo "
working...."

DERIV_TYPE_FOR_TIF=s

ls $DIRECTORY/*$DERIV_TYPE_FOR_TIF.tif | time parallel -j+0 --eta 'convert {}[0] -resize 1600x1600 -quality 100 {.}.jpg'

ls | awk '/^([0-9]+)\s.jpg$/ { printf("%s %04ds.jpg\n", $0, $1) }' | xargs -n2 mv

convert -verbose -density 300x300 -quality 100 "*.jpg" "$foldername.pdf"

find . -type f -name "*.jpg" -exec rm -f {} \; 

mv *.pdf /Volumes/ice/PDF_Storage
#mv *.pdf ~/Desktop

echo "
Success! PDF has been moved to PDF_Storage
"
