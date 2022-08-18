# # التكليف 01
#     لديك ال String التالي كما في المثال والمطلوب جلب ال Matches كما في الصورة
#     قم بكتابة ال Regular Expression Code لعمل المطلوب
#  return  E l  z e r  o
# "eeeeE llllLl lllzzZzzzz eroe operationr pollo "
# ===========================================================

import re

text = "eeeeE llllLl lllzzZzzzz eroe operationr pollo "

result = re.findall(r"\w ", text)
print(result)
