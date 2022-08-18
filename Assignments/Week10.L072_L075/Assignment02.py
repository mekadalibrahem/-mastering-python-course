# التكليف 02

#     قم بعمل Function بإسم get_names تقوم بإرجاع الأسماء التي تنتهي بحرف ال m
#     قم بإستخدام ال filter لتجعل هذه ال Function تمر على جميع عناصر ال List الموجودة في التكليف
#     قم بعمل متغير بإسم names وقم بتخزين نتيجة إستخدام ال filter فيه
#     قم بعمل Loop على المتغير names لتطبع جميع الأسماء الموجودة في القائمة
#     قم بإستخدام نفس المثال ولكن بإستخدام Lambda Function داخل ال Loop مباشرة

# friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]

# # Output
# "Wessam"
# "Essam"
# ########################################

def get_names(name):
    if name[-1] == "m":
        return True


friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]

names = filter(get_names, friends_filter)

for name in names:
    print(name)

print("=" * 30) 

#  with lambda function

names2 = filter((lambda name: name[-1] == "m"), friends_filter)
for name in names2:
    print(name)


# # Output
# "Wessam"
# "Essam"
