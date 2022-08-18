# التكليف 01
#     قم بكتابة ال Code التالي لتختبر نفسك ولا تقم بعمل Run له
#     بعد آخر سطر في ال Code قم بكتابة تعليق يحتوي على ال Output الذي سيخرج من وجهة نظرك
#     بعدها قم بعمل Run لترى النتيجة الخاصة بك سليمة أم لا
#     قم بوضع تعليق قبل كل سطر من الأسطر الموجودة في ال Code لتشرح كيف ظهرت هذه النتيجة

# values = (0, 1, 2)

# if any(values):

#   my_var = 0

# my_list = [True, 1,  1, ["A", "B"], 10.5, my_var]

# if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]):

#   print("Good")

# else:

#   print("Bad")

# ==================================================
values = (0, 1, 2)
#       t
if any(values):

    my_var = 0

my_list = [True, 1,  1, ["A", "B"], 10.5, my_var]
#     t                     f                   f
if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]):

    print("Good")

else:

    print("Bad")

# output : Good
