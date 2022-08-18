"""
034 - Boolean Operators 
link : https://www.youtube.com/watch?v=zN6ZYGSBKbM&list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs 

"""
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

print(age > 16 and country == "Egypt" and rank > 0)  # True
print(age > 16 and country == "KSA" and rank > 0)  # False

print(age > 40 or country == "KSA" or rank > 20)  # False
print(age > 40 or country == "Egypt" or rank > 20)  # True

print(age > 16)  # True
print(not age > 16)  # Not True = False