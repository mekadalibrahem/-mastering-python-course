'''
====================================
-- 100 - Regular Expressions Part 6 Re Module Search And FindAll 
-- link : https://www.youtube.com/watch?v=UKA-3O7XwPs&list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs 
====================================
'''
# ---------------------------------------------------------
# -- Regular Expressions =&gt; Re Module Search And FindAll --
# ---------------------------------------------------------
# search()  =&gt; Search A String For A Match And Return A First Match Only
# findall() =&gt; Returns A List Of All Matches and Empty List if No Match
# ---------------------------------------------------------------------
# Email Pattern =&gt; [A-z0-9\.]+@[A-z0-9]+\.(com|net|org|info)
# ----------------------------------------------------------

import re

my_search = re.search(r"[A-Z]{2}", "OOsamaEElzero")

print(my_search)
print(my_search.span())
print(my_search.string)
print(my_search.group())

is_email = re.search(r"[A-z0-9\.]+@[A-z0-9]+\.(com|net)", "os@osama.com")

if is_email:

  print("This is A Valid Email")

  print(is_email.span())
  print(is_email.string)
  print(is_email.group())

else:

  print("This is Not A Valid Email")

email_input = input("Please Write Your Email: ")

search = re.findall(r"[A-z0-9\.]+@[A-z0-9]+\.com|net", email_input)

empty_list = []

if search != []:

  empty_list.append(search)

  print("Email Added")

else:

  print("Invalid Email")

for email in empty_list:

  print(email)