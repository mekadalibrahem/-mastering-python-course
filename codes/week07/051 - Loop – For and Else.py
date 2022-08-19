"""
051 - Loop – For and Else 
link : https://www.youtube.com/watch?v=4YolrVX6f1Q&list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs
"""
# -----------------
# -- Loop => For --
# -----------------
# for item in iterable_object :
#   Do Something With Item
# -----------------------------
# item Is A Vairable You Create and Call Whenever You Want
# item refer to the current position and will run and visit all items to the end
# iterable_object => Sequence [ list, tuples, set, dict, string of charcaters, etc ... ]
# ---------------------------------------------------------------

myNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in myNumbers:

  # print(number * 17)

  if number % 2 == 0:  # Even

    print(f"The Number {number} Is Even.")

  else:

    print(f"The Number {number} Is Odd.")

else:

  print("The Loop Is Finished")

myName = "Osama"

for letter in myName:

  print(f" [ {letter.upper()} ] ")