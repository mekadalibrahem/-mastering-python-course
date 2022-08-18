# التكليف 01

#     قم بكتابة ال Code المناسب داخل ال Loop لتظهر النتيجة كما في المثال “Elzero”
#     لا تقم بتعديل أي شيء موجود مسبقا في ال Code

# my_list = ["E", "Z", "R", 1, 2, 3]
# my_tuple = ("L", "E", "O")
# my_data = []

# for data in zip(my_list, my_tuple):
#   # Write Your Code Here

# print(final_string) # Elzero
# ===========================================================

my_list = ["E", "Z", "R", 1, 2, 3]
my_tuple = ("L", "E", "O")
my_data = []

for data in zip(my_list, my_tuple):
    for i in data:
        my_data.append(i)


print(("".join(my_data)).capitalize())  # Elzero
