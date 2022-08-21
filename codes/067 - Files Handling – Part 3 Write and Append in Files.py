'''
====================================
-- 067 - Files Handling – Part 3 Write and Append in Files 
-- link : https://www.youtube.com/watch?v=FBcElrNaiZQ&list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs 
====================================
'''
# -----------------------------------------------
# -- File Handling =&gt; Write and Append In File --
# -----------------------------------------------

myFile = open("D:\Python\Files\osama.txt", "w")
myFile.write("Hello\n")
myFile.write("Third Line")

myFile = open(r"D:\Python\Files\fun.txt", "w")
myFile.write("Elzero Web School\n" * 1000)

myList = ["Oasma\n", "Ahmed\n", "Sayed\n"]

myFile = open("D:\Python\Files\osama.txt", "w")
myFile.writelines(myList)

myFile = open("D:\Python\Files\osama.txt", "a")
myFile.write("Elzero")