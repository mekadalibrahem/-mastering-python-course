'''
====================================
-- 058 - Function Packing, Unpacking Arguments 
-- link : https://www.youtube.com/watch?v=61i7VvPLVns&list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs 
====================================
'''
# -------------------------------------------------
# -- Function Packing, Unpacking Arguments *Args --
# -------------------------------------------------

print(1, 2, 3, 4)

myList = [1, 2, 3, 5]

print(myList)
print(*myList)

def say_hello(*peoples):  # n1, n2, n3, n4

  for name in peoples:

    print(f"Hello {name}")

say_hello("Osama", "Ahmed", "Sayed", "Mahmoud")

def show_details(name, *skills):

  print(f"Hello {name} Your Skills Is: ")

  for skill in skills:

    print(skill)

show_details("Osama", "Html", "CSS", "JS")
show_details("Ahmed", "Html", "CSS", "JS", "Python", "PHP", "MySQL")