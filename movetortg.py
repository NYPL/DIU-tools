#!/usr/bin/env python

import os
import subprocess
# provides a nice progress bar
import tqdm
import textwrap


output_folder = raw_input("\nPlease drag in the folder you would like to send to rtg and press [Enter]:\n\n").rstrip()
rtg_folder = '/Volumes/ice/rtg'

def check_for_spaces():
	if ' ' in output_folder:
		print('\nPlease remove spaces from your folder name and try again. Exiting.\n')
		exit()
	else:
		print('\nYour folder name is computer readable.\n')
		pass

def check_for_rename():
	for file in os.listdir(output_folder):
		if not len(file) > 9 and 's' not in file or 'u' not in file:
			print(textwrap.fill('There are files in your folder that need to be renamed. Please rename and try again. Exiting.'))
			exit('\n') 

def get_files():
	file_dict = {}
	file_dict[output_folder] = [file for file in os.listdir(output_folder) if 's.tif' in file or 'u.tif' in file and len(file) > 9]

	return file_dict

def move_files(file_dict):

	for file in tqdm.tqdm(file_dict[output_folder]):
		cmd = "rsync -ratvhP --progress --remove-source-files '{}' '{}'".format(os.path.join(output_folder, file), rtg_folder)
		pro = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, 
							stderr=subprocess.STDOUT, preexec_fn=os.setsid)

def main():
	check_for_spaces()
	check_for_rename()
	fileget = get_files()
	move_files(fileget)


if __name__ == '__main__':
	main()

