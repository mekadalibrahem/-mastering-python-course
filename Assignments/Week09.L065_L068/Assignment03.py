# التكليف 03

# قم بالتكملة على ما سبق في التكليف الأول
# قم بفتح الملف txt1.txt
# في السطر الأول قم بطباعة عدد الأسطر الموجودة داخل الملف
# في السطر الثاني قم بحساب عدد الكلمات الموجودة في الملف
# في الصف الثالث قم بطباعة عدد ال Characters الموجودة في الملف
# في السطر الرابع قم بطباعة كم عدد المرات التي وجد فيها الحرف “l”
#  Output
# "Number Of Lines Is => 51"
# "Number Of Words Is => 255"
# "Number Of Chars Is => 1268"
# "Number Of "l" Char Is => 102"
# ===================================================


import os


current_file = os.path.abspath(__file__)
current_folder = os.path.dirname(current_file)
file_path = current_folder + "\\python\\text1.txt"
myfile = open(file_path, "r")

count_line = 0
count_word = 0
count_char = 0
count_char_of_l = 0

for line in myfile:
    count_line += 1
    count_char += len(line)
    words = line.split()
    count_word += len(words)
    count_l_in_line = line.count("l")
    count_char_of_l += count_l_in_line

    # print(line)

count_char -= count_word -1
myfile.close()
myfile = open(file_path, "a")
myfile.write("\n")
myfile.write(f"Number Of Lines Is => {count_line}\n")
myfile.write(f"Number Of Words Is => {count_word}\n")
myfile.write(f"Number Of Chars Is => {count_char}\n")
myfile.write(f"Number Of \"l\" Char Is => {count_char_of_l}\n")
myfile.close()

