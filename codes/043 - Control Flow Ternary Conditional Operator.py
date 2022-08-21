'''
====================================
-- 043 - Control Flow Ternary Conditional Operator 
-- link : https://www.youtube.com/watch?v=1E7z7r61b2s&list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs 
====================================
'''
# ----------------------------------
# -- Ternary Conditional Operator --
# ----------------------------------

country = "A"

if country == "Egypt" : print(f"The Weather in {country} Is 15")
elif country == "KSA" : print(f"The Weather in {country} Is 30")
else : print("Country is Not in The List")

# Short If

movieRate = 18
age = 18

if age &lt; movieRate :

  print("Movie S Not Good 4U") # Condition If True

else :

  print("Movie S Good 4U And Happy Watching") # Condition If False

print("Movie S Not Good 4U" if age &lt; movieRate else "Movie S Good 4U And Happy Watching")

# Condition If True | If Condition | Else | Condition If False