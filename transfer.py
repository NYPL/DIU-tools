#!/usr/bin/env python

import subprocess
import sys
import os
import textwrap


TARGETLIST = {"Bay1" : "bay1@10.128.121.18", "Bay2" : "diubay5@10.128.121.19", "Bay3" : "Bay3@10.128.121.20", "Bay4" : "duint-03@10.128.121.21", "Bay5" : "Bay5@10.128.121.22", "Bay6" : "diubay6@10.128.121.23", "Dinah" : "diunt-02@10.128.121.17", "SASB" : "sasbstudio@10.128.32.131", "QC1" : "diuimac@10.128.121.24", "QC2" : "DIU@10.128.121.25", "QC3" : "diunt-01@10.128.121.26"}

print

print(textwrap.fill("This script will help you transfer files from your computer to another in the lab or vice versa. Your answers to the questions that follow will guide the process."))

print

ANSWER = raw_input("Are the files you would like to transfer on this computer? Y or N? ")

print

if ANSWER == "Y" or ANSWER == "y":

	print

	print(textwrap.fill("\nPlease drag in the folder you would like to transfer to another computer and press [Enter]:\n")).strip()

	DIRECTORY = raw_input('\n').strip()

	print

	print "\nWhich computer would you like your files to be tranferred to?\n" 
	
	print(textwrap.fill("Please type the name of a computer from this list [Bay1 Bay2 Bay3 Bay4 Bay5 Bay6 SASB QC1 QC2 QC3] and press [Enter]: "))
	
	inp = raw_input("\n")

	print

	if inp in TARGETLIST:
	    print
	else:
	    print('\n%s is not a DIU computer. please try again.\n') %inp 
	    sys.exit(0) 

	for key in inp.split():
	    try:
	        
		HOST=TARGETLIST[key]
		# Ports are handled in ~/.ssh/config since we use OpenSSH
		COMMAND="ls -h /Volumes"

		ssh = subprocess.Popen(["ssh", "%s" % HOST, COMMAND],
		                       shell=False,
		                       stdout=subprocess.PIPE,
		                       stderr=subprocess.PIPE)
		result = ssh.stdout.read()
		if result == []:
		    error = ssh.stderr.readlines()
		    print >>sys.stderr, "ERROR: %s" % error
		else:
		    print result

	    except KeyError:
	        continue

	print(textwrap.fill("Please copy and paste the name of the hard drive you would like to transfer files to and press [Enter]: "))

	LOCATION = raw_input("\n")

	print

	filepath = DIRECTORY
	hostname = TARGETLIST[key]
	remotepath = LOCATION

	subprocess.Popen(["time","scp","-r", filepath, hostname+':'+'/'+'Volumes'+'/'+remotepath]).wait()

	for your_dir in LOCATION:
	    for root, dirs, files in os.walk(LOCATION):
	        for d in dirs:
	            os.chmod(os.path.join(root, d), 0o777)
	        for f in files:
	            os.chmod(os.path.join(root, f), 0o777)

else: 
	print "\nWhere are the files you would like to transfer located?\n"

	print(textwrap.fill("Please type the name of a computer from this list [Bay1 Bay2 Bay3 Bay4 Bay5 Bay6 SASB QC1 QC2 QC3] and press [Enter]:  ")) 
	
	inp = raw_input('\n').strip()

	print

	if inp in TARGETLIST:
	    print
	else:
	    print('\n%s is not a DIU computer. please try again.\n') %inp 
	    sys.exit(0) 

	for key in inp.split():
	    try:
	        
		HOST=TARGETLIST[key]
		# Ports are handled in ~/.ssh/config since we use OpenSSH
		COMMAND="ls /Volumes"

		ssh = subprocess.Popen(["ssh", "%s" % HOST, COMMAND],
		                       shell=False,
		                       stdout=subprocess.PIPE,
		                       stderr=subprocess.PIPE)
		result = ssh.stdout.read()
		if result == []:
		    error = ssh.stderr.readlines()
		    print >>sys.stderr, "ERROR: %s" % error
		else:
		    print result

	    except KeyError:
	        continue

	print(textwrap.fill("Please copy and paste the name of the hard drive where your files are located and press [Enter]: "))

	LOCATION = raw_input("\n").strip()

	print
	print

	COMMAND2="ls /Volumes"+'/'+LOCATION

	ssh = subprocess.Popen(["ssh", "%s" % HOST, COMMAND2],
	                       shell=False,
	                       stdout=subprocess.PIPE,
	                       stderr=subprocess.PIPE)
	result = ssh.stdout.read()
	if result == []:
	    error = ssh.stderr.readlines()
	    print >>sys.stderr, "ERROR: %s" % error
	else:
	    print result

	print(textwrap.fill("Please copy and paste the name of the folder you would like to transfer to this computer and press [Enter]: "))

	REMOTEFOLDER = raw_input("\n").strip()

	for your_dir in REMOTEFOLDER:
	    for root, dirs, files in os.walk(REMOTEFOLDER):
	        for d in dirs:
	            os.chmod(os.path.join(root, d), 0o777)
	        for f in files:
	            os.chmod(os.path.join(root, f), 0o777)

	print
	print

	print(textwrap.fill("Please drag in the folder or hard drive on this computer where you would like your files to transfer to and press [Enter]: ")).strip()

	DIRECTORY = raw_input("\n").strip()

	print

	filepath = DIRECTORY
	hostname = TARGETLIST[key]
	remotepath = LOCATION
	remotedirectory = REMOTEFOLDER

	subprocess.Popen(["time","scp","-r", hostname+':'+'/'+'Volumes'+'/'+remotepath+'/'+remotedirectory, filepath]).wait()

	for your_dir in REMOTEFOLDER:
	    for root, dirs, files in os.walk(REMOTEFOLDER):
	        for d in dirs:
	            os.chmod(os.path.join(root, d), 0o777)
	        for f in files:
	            os.chmod(os.path.join(root, f), 0o777)
