""" 
048 - Loop – While Training’s 
link  : https://www.youtube.com/watch?v=9rU2fImqSR4&list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs

"""
# ----------------------------
# -- Loop => While Training --
# ----------------------------
# while condition_is_true
#   Code Will Run Until Condition Become False
# -----------------------

myF = ["Os", "Ah", "Ga", "Al", "Ra", "Sa", "Ta", "Ma", "Mo", "Wa"]

# print(len(myF))  # List Length [10]

a = 0

while a < len(myF):  # a < 10

  print(f"#{str(a + 1).zfill(3)} {myF[a]}")

  a += 1  # a = a + 1

else:

  print("All Friends Printed To Screen.")

# print(myF[0])
# print(myF[1])
# print(myF[2])
# print(myF[3])
# print(myF[4])
# print(myF[5])
# print(myF[6])
# print(myF[7])
# print(myF[8])
# print(myF[9])