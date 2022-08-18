# التكليف 02

#     لديك ال String التالي كما في المثال والمطلوب جلب ال Matches كما في الصورة
#     قم بكتابة ال Regular Expression Code لعمل المطلوب
#  return Elzero
# "EElzero11 LElzero111 ZElzero1111 EElzero11111 RElzero111111 OElzero1111111"
# ########################################
import re
text = "EElzero11 LElzero111 ZElzero1111 EElzero11111 RElzero111111 OElzero1111111"
result = re.search(r"[L](Elzero)", text)

print(result.group(1))
