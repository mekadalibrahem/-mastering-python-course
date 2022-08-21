'''
====================================
-- 065 - Files Handling – Part 1 Intro 
-- link : https://www.youtube.com/watch?v=6TFJs9uzEjI&list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs 
====================================
'''
# -------------------
# -- File Handling --
# -------------------
# "a" Append  Open File For Appending Values, Create File If Not Exists
# "r" Read    [Default Value] Open File For Read and Give Error If File is Not Exists
# "w" Write   Open File For Writing, Create File If Not Exists
# "x" Create  Create File, Give Error If File Exists
# --------------------------------------------------

import os

# Main Current Working Directory
print(os.getcwd())

# Directory For The Opened File
print(os.path.dirname(os.path.abspath(__file__)))

# Change Current Working Directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

print(os.getcwd())

print(os.path.abspath(__file__))

file = open(r"D:\Python\Files\nfiles\osama.txt")

file = open("D:\Python\Files\osama.txt")