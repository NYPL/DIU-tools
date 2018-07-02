#!/bin/bash

#find all folders indicated with a particular string 

#if there are .tiff files in those folders, move those files into rtg using rsync 

#log the action to a log file
DATE=$(date +%Y%m%d-%H%M%S)
ICE="/Volumes/ice"
RTG="/Volumes/ice/rtg/"
LOGFILE="/Users/Eric/Desktop/Logs/${DATE}_ICEnightmoves.log"

find "${ICE}" -type d -iname 'X*X' -exec rsync -rathvP --exclude="./" --exclude="jpegs" --exclude="jp2" --exclude="QC" --exclude="*.jpg" --exclude="CaptureOne" --exclude-from '/Volumes/ice/exclude2.txt' --log-file="${LOGFILE}" --log-file-format="${DATE} '%f' %l " --remove-source-files "{}/" "${RTG}" \;  
