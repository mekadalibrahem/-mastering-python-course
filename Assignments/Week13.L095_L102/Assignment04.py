# التكليف 04

#     لديك ال String التالي كما في المثال والمطلوب جلب ال Matches كما في الصورة
#     قم بكتابة ال Regular Expression Code لعمل المطلوب

# http://www.elzero.org:8888/link.php
# https://elzero.org:8888/link.php
# http://www.elzero.com/link.py
# https://elzero.com/link.py
# http://www.elzero.net
# https://elzero.net

# output : 

# http://www.elzero.org:8888/link.php
# https://elzero.org:8888/link.php
# http://www.elzero.com/link.py
# https://elzero.com/link.py
# =========================================================

#  (https?://(www)?\.?\w+\.(org|com):?(\d+)?/\w+\.(php|py))
import re
text = """ 
http://www.elzero.org:8888/link.php
https://elzero.org:8888/link.php
http://www.elzero.com/link.py
https://elzero.com/link.py
http://www.elzero.net
https://elzero.net
"""
result = re.findall(r"(https?://(www)?\.?\w+\.(org|com):?(\d+)?/\w+\.(php|py))", text , re.MULTILINE )

print(result)
