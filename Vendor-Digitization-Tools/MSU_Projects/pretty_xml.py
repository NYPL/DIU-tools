#!/usr/bin/env python3

from bs4 import BeautifulSoup
from xml.etree import ElementTree


## makes XML a bit easier to read

file = '/Users/diunt-02/Desktop/DataPublishing_1.xml'

bs = BeautifulSoup(open(file), 'xml')
pretty_xml = (bs.prettify())

new_file = open('pretty.xml', 'w')
new_file.write(pretty_xml)
