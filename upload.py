#!/usr/bin/env python

import os
import stat
import subprocess
# modules for parallel work
import multiprocessing
from joblib import Parallel, delayed
# provides a nice progress bar
import tqdm


output_folder = raw_input("\nPlease drag in the folder you would like to upload to the server and press [Enter]:\n\n").rstrip()
server_folder = raw_input("\nPlease drag in the folder on the server you'd like to upload to and press [Enter]\n\n").rstrip()
QC_folder = os.path.join(server_folder,'QC')

def check_for_spaces():
	if ' ' in output_folder or ' ' in server_folder:
		print('Check folder and hard drive names for spaces')
		exit()
	else:
		print('\nYour folder and hard drive names are computer readable\n')
		pass

def set_folder_permissions():
	os.chmod(server_folder, 0o777)
	print('Your server folder permissions have been set to {} (0777 is most permissive)\n'.format(oct(stat.S_IMODE(os.lstat(server_folder).st_mode))))

def get_files():
	file_dict = {}
	file_dict[output_folder] = [file for file in os.listdir(output_folder) if '.tif' in file]

	return file_dict, len(file_dict[output_folder])

def move_files(file_dict, length):

	for file in tqdm.tqdm(file_dict[output_folder]):
		cmd = "rsync -ratvhP --progress '{}' '{}'".format(os.path.join(output_folder, file), server_folder)
		pro = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, 
							stderr=subprocess.STDOUT, preexec_fn=os.setsid)
		stdout = pro.communicate()[0]
		stdout = stdout.decode("utf-8")

def make_folder():
	try:
		os.mkdir(QC_folder)
	except:
		pass

def create_jpg(i):
	cmd = 'convert {}[0] -resize 3500x3500 -quality 100 {}.jpg'.format(os.path.join(server_folder,i), os.path.join(QC_folder,os.path.basename(i[0:-4])))
	pro = subprocess.call(cmd, stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid) 

def parallel_processing(file_dict):
	num_cores = multiprocessing.cpu_count()
	Parallel(n_jobs=num_cores)(delayed(create_jpg)(file) for file in tqdm.tqdm(file_dict[output_folder]))

def main():
	check_for_spaces()
	set_folder_permissions()
	fileget = get_files()
	move_files(fileget[0], fileget[1])
	make_folder()
	parallel_processing(fileget[0])

if __name__ == '__main__':
	main()


