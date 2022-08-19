''' 
062 - Function Scope 
link :  https://www.youtube.com/watch?v=VQHLn1wuDBw&list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs
'''
# --------------------
# -- Function Scope --
# --------------------

x = 1  # Global Scope

def one():

  global x

  x = 2

  print(f"Print Variable From Function Scope {x}")

def two():

  x = 10

  print(f"Print Variable From Function Scope {x}")

one()
print(f"Print Variable From Global Scope {x}")
two()
print(f"Print Variable From Global Scope After One Function Is Called {x}")