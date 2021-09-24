"""Exercise 1: Write a Python program to scan a specified directory
and identify the sub directories and files.
"""

import os

FOLDER  = "test_folder"
base_dir = os.path.dirname(__file__)
path = os.path.join(base_dir, FOLDER)

dirlist = os.listdir(path)

print(dirlist)