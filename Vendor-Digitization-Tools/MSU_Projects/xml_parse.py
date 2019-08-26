#!/usr/bin/env python3

import os
import glob
from xml.etree import ElementTree as ET
import csv


header = ('folder', 'title', 'pub_date', 'release_date')
def main():

    with open('test.csv', 'w', encoding='utf-8-sig') as f:
        w = csv.DictWriter(f, fieldnames=header)
        w.writeheader()


        for filename in glob.glob('/Volumes/parking/MOMW_NYPL/*/*.xml'):
                tree = ET.parse(filename)
                root = tree.getroot()
                base_file = os.path.basename(filename)
                base_folder = os.path.splitext(base_file)[0]
                folder = "Folder: " + str(base_folder)
                print(folder)
                for fullTitle in root.iter('fullTitle'):
                    full_title = fullTitle.text
                for pubDate in root.iter('pubDate'):
                    pub_date = pubDate.text
                for releaseDate in root.iter('releaseDate'):
                    rel_date = releaseDate.text


                w.writerow({'folder':folder, 'title':full_title, 'pub_date':pub_date, 'release_date':rel_date})




if __name__ == '__main__':
    main()
