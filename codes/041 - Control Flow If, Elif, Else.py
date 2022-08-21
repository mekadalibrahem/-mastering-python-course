'''
====================================
-- 041 - Control Flow If, Elif, Else 
-- link : https://www.youtube.com/watch?v=v8ZehXS3XF0&list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs 
====================================
'''
# --------------------
# --  Control Flow  --
# -- If, Elif, Else --
# -- Make Decisions --
# --------------------

uName = "Osama"
uCountry = "Kuwait"
cName = "Python Course"
cPrice = 100

if uCountry == "Egypt":

  print(f"Hello {uName} Because You Are From {uCountry}")
  print(f"The Course \"{cName}\" Price Is: ${cPrice - 80}")

elif uCountry == "KSA":

  print(f"Hello {uName} Because You Are From {uCountry}")
  print(f"The Course \"{cName}\" Price Is: ${cPrice - 60}")

elif uCountry == "Kuwait":

  print(f"Hello {uName} Because You Are From {uCountry}")
  print(f"The Course \"{cName}\" Price Is: ${cPrice - 50}")

else:

  print(f"Hello {uName} Because You Are From {uCountry}")
  print(f"The Course \"{cName}\" Price Is: ${cPrice - 30}")