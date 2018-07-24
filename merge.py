#!/usr/bin/env python

import subprocess
import os
import tqdm
import textwrap


left_computer = raw_input("\nPlease drag in your Capture folder from the session you'd like to copy TO (book scanner left):\n\n").rstrip()
right_computer = raw_input("\nPlease drag in your Capture folder from the session you'd like to copy FROM (book scanner right):\n\n").rstrip()


def get_files(capture_path):

	capture_dict = {}

	for dir_path, subdir_list, file_list in os.walk(capture_path):
		file_list = [f for f in file_list if not f.startswith('.')]
		capture_dict[os.path.basename(dir_path)] = {}
		capture_dict[os.path.basename(dir_path)][dir_path] = file_list

	for key in capture_dict:
		if 'Settings' in key:
			settings = key
			for path in capture_dict[key]:
				settings_path = path

	return capture_dict, settings, settings_path

def check_for_dupes(key, ldict, rdict, lpath, rpath):

	rename = 0
	rename_list = []

	for file in rdict[key][rpath]:
		if file in ldict[key][lpath]:
			rename = rename + 1
			rename_list.append(os.path.basename(file))

	if rename > 0:
		for i in rename_list:
			print(i)
		print('\n')
		print(textwrap.fill('Captures not moved in order to prevent overwrites. Please rename files listed above and try again. \n'))
		exit('\n')

def move_files(key, ldict, rdict, lpath, rpath):

	safely_moved = 0

	for file in tqdm.tqdm(rdict[key][rpath]):
		cmd = "rsync -ratvhP --progress '{}' '{}'".format(os.path.join(rpath, file), lpath)
		pro = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, 
							stderr=subprocess.STDOUT, preexec_fn=os.setsid)
		stdout = pro.communicate()[0]
		stdout = stdout.decode("utf-8")
		print(stdout)
		safely_moved = safely_moved + 1

	total_count = len([x for x in os.listdir(lpath) if x != 'CaptureOne'])

	return safely_moved, total_count

class CaptureOneSession():

	def __init__(self, capture_path):
		fileget = get_files(capture_path)
		self.capture_path = capture_path
		self.capture_dict = fileget[0]
		self.proxies_path = capture_path + '/CaptureOne/Cache/Proxies'
		self.thumbnails_path = capture_path + '/CaptureOne/Cache/Thumbnails'
		self.settings_path = fileget[2]
		self.settings = fileget[1]

def main():

	left = CaptureOneSession(left_computer)
	right = CaptureOneSession(right_computer)
	check_for_dupes('Capture', left.capture_dict, right.capture_dict, left.capture_path, right.capture_path)
	capture = move_files('Capture', left.capture_dict, right.capture_dict, left.capture_path, right.capture_path)
	move_files('Proxies', left.capture_dict, right.capture_dict, left.proxies_path, right.proxies_path)
	move_files('Thumbnails', left.capture_dict, right.capture_dict, left.thumbnails_path, right.thumbnails_path)
	move_files(right.settings, left.capture_dict, right.capture_dict, left.settings_path, right.settings_path)

	print('\n\n\nRenamer report: \n')
	print(str('{} captures merged into new combined session ({} captures total).\n'.format(capture[0], capture[1])))

if __name__ == '__main__':
	main()
