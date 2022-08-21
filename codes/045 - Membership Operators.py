'''
====================================
-- 045 - Membership Operators 
-- link : https://www.youtube.com/watch?v=FGnMK1y9TkE&list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs 
====================================
'''
# --------------------------
# -- Membership Operators --
# --------------------------
# in
# not in
# --------------------------

# String

name = "Osama"
print("s" in name)
print("a" in name)
print("A" in name)

print("#" * 50)

# List

friends = ["Ahmed", "Sayed", "Mahmoud"]
print("Osama" in friends)
print("Sayed" in friends)
print("Mahmoud" not in friends)

print("#" * 50)

# Using In and Not In With Condition

countriesOne = ["Egypt", "KSA", "Kuwait", "Bahrain", "Syria"]
countriesOneDiscount = 80

countriesTwo = ["Italy", "USA"]
countriesTwoDiscount = 50

myCountry = "Italy"

if myCountry in countriesOne:

  print(f"Hello You Have A Discount Equal To ${countriesOneDiscount}")

elif myCountry in countriesTwo:

  print(f"Hello You Have A Discount Equal To ${countriesTwoDiscount}")

else:

  print("You Have No Discount")