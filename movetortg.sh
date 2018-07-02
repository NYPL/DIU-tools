#!/bin/bash

echo "
Please drag in your folder to send to rtg and press [Enter]: 
"
read DIRECTORY

cd $DIRECTORY

echo "
Working....
"


digits=$(ls | grep -x '.\{10,\}')


if ! $digits ;
	then ls | grep -x '.\{10,\}' | time rsync --progress -ratvhP --exclude=".*" --exclude="jpegs" --exclude="QC" --exclude="*.jpg" --exclude="CaptureOne" --remove-source-files --files-from - ./ /Volumes/ice/rtg 
		echo " 
Success! Your files have been moved to rtg
"
	else 
		echo " 
Either no files are in your input folder or they need to be renamed
"
fi


