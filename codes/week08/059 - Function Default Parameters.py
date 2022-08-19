''' 
059 - Function Default Parameters 

link : https://www.youtube.com/watch?v=BNXasw_j4sY&list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs

'''
# ---------------------------------
# -- Function Default Parameters --
# ---------------------------------

def say_hello(name="Unknown", age="Unknown", country="Unknown"):

  print(f"Hello {name} Your Age is {age} and Your Country Is {country}")

say_hello("Osama", 36, "Egypt")
say_hello("Mahmoud", 28, "KSA")
say_hello("Sameh", 38)
say_hello("Ramy")
say_hello()