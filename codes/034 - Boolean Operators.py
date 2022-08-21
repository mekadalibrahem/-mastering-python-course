'''
====================================
-- 034 - Boolean Operators 
-- link : https://www.youtube.com/watch?v=zN6ZYGSBKbM&list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs 
====================================
'''
# -----------------------
# -- Boolean Operators --
# -----------------------
# and
# or
# not
# -----------------------

age = 36
country = "Egypt"
rank = 10

print(age &gt; 16 and country == "Egypt" and rank &gt; 0)  # True
print(age &gt; 16 and country == "KSA" and rank &gt; 0)  # False

print(age &gt; 40 or country == "KSA" or rank &gt; 20)  # False
print(age &gt; 40 or country == "Egypt" or rank &gt; 20)  # True

print(age &gt; 16)  # True
print(not age &gt; 16)  # Not True = False