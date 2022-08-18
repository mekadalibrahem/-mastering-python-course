# التكليف 02

#     قم بكتابة ال Code المناسب داخل ال Loop لتظهر النتيجة كما في المثال “Elzero”
#     لا تقم بتعديل أي شيء موجود مسبقا في ال Code

# my_list1 = ["E", "L", "Z", "E", "R", "O", 1, 2]
# my_tuple = ("E", "Z", "R", 1, 2, "E", "R", "O")
# my_list2 = ("L", "E", "O", 1, 2, "E", "R", "O")
# my_data = []

# for item1, item2, item3 in zip(my_list1, my_tuple, my_list2):
#   # Write Your Code Here

# print(final_string)
# ########################################

my_list1 = ["E", "L", "Z", "E", "R", "O", 1  , 2  ]
my_tuple = ("E", "Z", "R", 1  , 2  , "E", "R", "O")
my_list2 = ("L", "E", "O", 1  , 2  , "E", "R", "O")
my_data = []

for item1, item2, item3 in zip(my_list1, my_tuple, my_list2):
  # Write Your Code Here
  if str(item1).isalpha()  :
      my_data.append(item1)

print(("".join(my_data)).capitalize())