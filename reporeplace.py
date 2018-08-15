#!/usr/bin/env python

import subprocess

raw_input("\nPlease click 'Copy all Capture IDs' on your work order and press [return].\n\n").rstrip()

def read_from_clipboard():
    id_str = subprocess.check_output(
        'pbpaste')
    return id_str

def find_replace(old_id_str):
	new_id_str = old_id_str.replace(', ', '\n')
	return new_id_str 

def write_to_clipboard(new_id_str):
    process = subprocess.Popen(
        'pbcopy', stdin=subprocess.PIPE)
    process.communicate(new_id_str)
    print('\nYour Image IDs have been copied to the clipboard.\n\nPlease paste (command + v) into Image Get for repo check.\n')

def main():
	old_id_str = read_from_clipboard()
	new_id_str = find_replace(old_id_str)
	write_to_clipboard(new_id_str)

if __name__ == '__main__':
	main()

