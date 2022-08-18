# التكليف 01

#     قم بإستدعاء أي Module يقوم بإنشاء أرقام عشوائية
#     قم بتوليد رقم عشوائي ما بين 10 و 50 واطبع الرسالة مثل المثال
#     في السطر الثاني قم بتوليد رقم عشوائي زوجي فقط ما بين 2 و 10 شاهد المثال لترى الرسالة
#     في السطر الثالث قم بتوليد رقم عشوائي فردي فقط ما بين 1 و 9 شاهد المثال لترى الرسالة
#     قم بطباعة جميع ال Methods الموجودة في ال Module الذي إستخدمته

# "Random Number Between 10 And 50 =>" "Show The Random Number Here"
# "Random Even Number Between 2 And 10 =>" "Show The Random Even Number Here"
# "Random Odd Number Between 1 And 9 =>" "Show The Random Odd Number Here"

# Module Methods Content Here
# ===========================================================

import random

print(random.randrange(10, 50))
print(random.randrange(2, 10, 2))
print(random.randrange(1, 9, 2))

print(dir(random))
