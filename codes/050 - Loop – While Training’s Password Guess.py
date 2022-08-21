'''
====================================
-- 050 - Loop – While Training’s Password Guess 
-- link : https://www.youtube.com/watch?v=7NIcsmfHIrg&list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs 
====================================
'''
# ----------------------------
# -- Loop =&gt; While Training --
# -- Simple Password Guess --
# ----------------------------

tries = 4

mainPassword = "Osama@123"

inputPassword = input("Write Your Password: ")

while inputPassword != mainPassword:  # True

  tries -= 1  # tries = tries - 1

  print(f"Wrong Password, { 'Last' if tries == 0 else tries } Chance Left")

  inputPassword = input("Write Your Password: ")

  if tries == 0:

    print("All Tries Is Finished.")

    break

    print("Will Not Print")

else:

  print("Correct Password")