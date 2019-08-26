#!/usr/bin/env python3

## will move all files of a certain extension to a folder that is made at the parent directory level
##currently will only go down one subdirectory level - this can be changed!


import os
import shutil

current_path = os.getcwd()


def main():

    ## change this to match the extension you'd like to move
    ## for rest of script, just sub "xml" with what you'd like
    os.makedirs('./xml_files/')

    for child in os.scandir(current_path):
        if child.is_dir():
            for file in os.listdir(child.path):
                if file.endswith('xml'):
                    sourcepath = os.path.join(child, file)
                    newpath = os.path.join(current_path, 'xml_files/')
                    file_path = os.path.join(newpath, file)
                    if os.path.exists(file_path):
                        break
                    else:
                        shutil.copy2(sourcepath, newpath)




if __name__ == '__main__':
    main()
