# التكليف 01

#     قم بعمل Function بإسم remove_chars تزيل أول وآخر حرف من اي String
#     قم بإستخدام ال map لتجعل هذه ال Function تمر على جميع عناصر ال List الموجودة في التكليف
#     قم بعمل متغير بإسم cleaned_list وقم بتخزين نتيجة إستخدام ال map فيه
#     قم بعمل Loop على المتغير cleaned_list لتطبع جميع الأسماء الموجودة في القائمة
#     قم بإستخدام نفس المثال ولكن بإستخدام Lambda Function داخل ال Loop مباشرة

# friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]

# # Output
# "Eman"
# "Ahmed"
# "Sameh"
# "Osama"

# ===========================================================

def remove_chars(text):
    return text[1:-1]


friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]
cleaned_list = map(remove_chars, friends_map)
for cleaned_name in cleaned_list:
    print(cleaned_name)

#  with lambda funtion 
print("=" * 30) 
friends_map2 = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]

cleaned_list2 =  map( ( lambda name : name[1:-1] ) , friends_map2)
for cleaned_name in cleaned_list2:
    print(cleaned_name)



# # Output
# "Eman"
# "Ahmed"
# "Sameh"
# "Osama"
