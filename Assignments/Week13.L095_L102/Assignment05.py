# التكليف 04

#     لديك ال String التالي كما في المثال والمطلوب جلب ال Matches كما في الصورة
#     قم بكتابة ال Regular Expression Code لعمل المطلوب
#     يجب عليك عمل المطلوب ب 5 طرق مختلفة

# http
# https
# abcd
# abcd
# output: 
# http
# https
# =========================================================


import re
text = """ 
http
https
abcd
abcd
"""
# 1:  (https?)
# 2:  ^h\w+
# 3:  ^h\w+s?
# 3:  \w+(p|s)$
# 5:
result = re.findall(r"(https?)", text , re.MULTILINE )

print(result)
