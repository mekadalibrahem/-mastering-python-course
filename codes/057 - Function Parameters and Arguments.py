'''
====================================
-- 057 - Function Parameters and Arguments 
-- link : https://www.youtube.com/watch?v=CCMKMBGUxkc&list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs 
====================================
'''
# ---------------------------------------
# -- Function Parameters And Arguments --
# ---------------------------------------

a, b, c = "Osama", "Ahmed", "Sayed"

print(f"Hello {a}")
print(f"Hello {b}")
print(f"Hello {c}")

# def                     =&gt; Function Keyword [Define]
# say_hello()             =&gt; Function Name
# name                    =&gt; Parameter
# print(f"Hello {name}")  =&gt; Task
# say_hello("Ahmed")      =&gt; Ahmed is The Argument

def say_hello(n):

  print(f"Hello {n}")

say_hello(a)
say_hello(b)
say_hello(c)

def addition(n1, n2):

  print(n1 + n2)

addition(100, 300)
addition(-50, 100)


def addition(n1, n2):

  if type(n1) != int or type(n2) != int:

    print("Only Integers Allowed")

  else:

    print(n1 + n2)

addition(100, 500)

def full_name(first, middle, last):

  print(f"Hello {first.strip().capitalize()} {middle.upper():.1s} {last.capitalize()}")

full_name("   osama   ", 'mohamed', "elsayed")