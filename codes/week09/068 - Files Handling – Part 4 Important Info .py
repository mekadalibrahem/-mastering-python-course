'''' 
068 - Files Handling – Part 4 Important Info  
link : https://www.youtube.com/watch?v=wwe40Ngpp3A&list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs
'''
# -------------------------------------
# -- File Handling => Important Info --
# -------------------------------------

import os

myFile = open("D:\Python\Files\osama.txt", "a")
myFile.truncate(5)

myFile = open("D:\Python\Files\osama.txt", "a")
print(myFile.tell())

myFile = open("D:\Python\Files\osama.txt", "r")
myFile.seek(11)
print(myFile.read())

os.remove("D:\Python\Files\osama.txt")