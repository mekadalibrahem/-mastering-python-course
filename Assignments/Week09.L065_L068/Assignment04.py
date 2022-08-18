# التكليف 04

# قم بالتكملة على ما سبق في التكليف الأول
# بطريقة برمجية وبواسطة ال Loop قم بحذف آخر عشر ملفات txt
# بعد إتمام العملية السابقة بنجاح سيكون آخر ملف عندك إسمه txt40.txt


# =========================================================


import os


current_file = os.path.abspath(__file__)
current_folder = os.path.dirname(current_file)
folder_path = current_folder + "\\python"
list_files = os.listdir(folder_path)

for i in range(41 ,51):
    os.remove(f"{folder_path}\\text{str(i)}.txt")

