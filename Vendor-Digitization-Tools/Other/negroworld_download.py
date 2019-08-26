#!/usr/bin/env python3

import requests
import os
from bs4 import BeautifulSoup

##script used to download PDFs from Negro World Micro Site. Could be adjusted to download PDFs and images from other sites as well. 

url = "https://blacknewyorkers-nypl.org/negro-world/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

path = "/Volumes/ice/Katie/NegroWorld/Volumes"


for items in soup.findAll("div", {"class": "wpb_accordion_section group"}):
    for volumes in items.findAll("h3", {"class": "wpb_accordion_header ui-accordion-header"}):
        volumes = volumes.text

        volumes = volumes.replace(" ", "_")

        folder = path + "/" + volumes
        if os.path.exists(folder):
            print("Exists!")
        else:
            os.mkdir(folder)

    for td in items.findAll("td"):
        for ref in td.findAll("a"):
            link = ref.get("href")

            text = ref.text
            text = text.replace(" ", "_")
            text = text.replace(".", "_")

            download_folder = path + "/" + volumes + "/" + text
            if os.path.exists(download_folder):
                print(download_folder + " exists!")
            else:
                os.mkdir(download_folder)


            download_file = download_folder + "/" + text + ".pdf"
            if os.path.exists(download_file):
                print("Already downloaded " + download_file + "!")
            else:
                if link != "http://sample.pdf":
                    r = requests.get(link)
                    if r.status_code == 200:
                        print("Getting " + download_file + "!")
                        with open(download_file, "wb") as f:
                            f.write(r.content)
                    else:
                        with open(path + "/error_log.txt", "a") as f:
                            f.write("ERROR: " + link + "\n")
