# التكليف 02

#     قم بالتكملة على ما سبق في التكليف الأول
#     قم بفتح الملف txt1.txt
#     إترك السطر الأول كما هو والمكتوب فيه Elzero Web School => 1
#     من بداية السطر الثاني قم بكتابة Appended => Elzero Web School خمسون مرة كل واحدة على سطر مختلف

# # Output
# Elzero Web School => 1
# Appended => Elzero Web School
# Appended => Elzero Web School
# .
# .
# Appended => Elzero Web School
# Appended => Elzero Web School
# ########################################


import os


def write_text_in_file_mult(file, text, count, mode="a"):
    file = open(file, mode)
    for i in range(count):
        file.write(text)

    file.close()


current_file = os.path.abspath(__file__)
current_folder = os.path.dirname(current_file)
file_to_write = current_folder + "\\python\\text1.txt"
write_text_in_file_mult(file_to_write, "\nAppended => Elzero Web School", 50)
