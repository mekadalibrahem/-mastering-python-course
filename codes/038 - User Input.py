'''
====================================
-- 038 - User Input 
-- link : https://www.youtube.com/watch?v=2EY1CCnByK4&list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs 
====================================
'''
# ----------------
# -- User Input --
# ----------------

fName = input('What\'s Is Your First Name?')
mName = input('What\'s Is Your Middle Name?')
lName = input('What\'s Is Your Last Name?')

fName = fName.strip().capitalize()
mName = mName.strip().capitalize()
lName = lName.strip().capitalize()

print(f"Hello {fName} {mName:.1s} {lName} Happy To See You.")