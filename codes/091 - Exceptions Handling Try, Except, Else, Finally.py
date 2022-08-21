'''
====================================
-- 091 - Exceptions Handling Try, Except, Else, Finally 
-- link : https://www.youtube.com/watch?v=LBf_8txij3I&list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs 
====================================
'''
# -----------------------------------
# --      Exceptions Handling      --
# -- Try | Except | Else | Finally --
# -----------------------------------
# Try     =&gt; Test The Code For Errors
# Except  =&gt; Handle The Errors
# ----------------------------
# Else    =&gt; If No Errors
# Finally =&gt; Run The Code
# ------------------------

number = int(input("Write Your Age: "))

print(number)
print(type(number))

try:  # Try The Code and Test Errors

  number = int(input("Write Your Age: "))

  print("Good, This Is Integer From Try")

except:  # Handle The Errors If Its Found

  print("Bad, This is Not Integer")

else:  # If Theres No Errors

  print("Good, This Is Integer From Else")

finally:

  print("Print From Finally Whatever Happens")


try:

  # print(10 / 0)
  # print(x)
  print(int("Hello"))

except ZeroDivisionError:

  print("Cant Divide")

except NameError:

  print("Identifier Not Found")

except ValueError:

  print("Value Error Elzero")

except:

  print("Error Happens")