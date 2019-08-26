#!/usr/bin/env python3
## will validate a bag

import bagit

source_folder = input("Please drag over the bag that you would like to validate.\n--------\n\n")
folder_path = source_folder.replace('\\', '')
folder_path = folder_path.rstrip()

bag = bagit.Bag(folder_path)

print(f"\n--------\n\nValidating {folder_path}. \n\n--------\n\n")


try:
  bag.validate()
  print("Validating...")

except bagit.BagValidationError as e:
    for d in e.details:
        print("Checking details....")
        if isinstance(d, bagit.ChecksumMismatch):
            print("expected %s to have %s checksum of %s but found %s" %
                  (d.path, d.algorithm, d.expected, d.found))
