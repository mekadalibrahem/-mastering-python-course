'''
====================================
-- 080 - Date And Time – Format Date 
-- link : https://www.youtube.com/watch?v=Qa6p-eQ7k0U&list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs 
====================================
'''
# ----------------------------------
# -- Date and Time =&gt; Format Date --
# ----------------------------------
# https://strftime.org/
# ---------------------

import datetime

myBirthday = datetime.datetime(1982, 10, 25)

print(myBirthday)
print(myBirthday.strftime("%a"))
print(myBirthday.strftime("%A"))
print(myBirthday.strftime("%b"))
print(myBirthday.strftime("%B"))

print(myBirthday.strftime("%d %B %Y"))
print(myBirthday.strftime("%d, %B, %Y"))
print(myBirthday.strftime("%d/%B/%Y"))
print(myBirthday.strftime("%d - %B - %Y"))
print(myBirthday.strftime("%B - %Y"))