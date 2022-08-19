''' 
070 - Built In Functions Part 2  
link : https://www.youtube.com/watch?v=2ed3aomFliA&list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs
'''
# ------------------------
# -- Built In Functions --
# ------------------------
# sum()
# round()
# range()
# print()
# ------------------------

# sum(iterable, start)
a = [1, 10, 19, 40]
print(sum(a))
print(sum(a, 40))

# round(number, numofdigits)
print(round(150.501))
print(round(150.554, 2))

# range(start, end, step)
print(list(range(0)))
print(list(range(10)))
print(list(range(0, 20, 2)))

# print()
print("Hello @ Osama @ How @ Are @ You")
print("Hello", "Osama", "How", "Are", "You", sep=" | ")

print("First Line", end=" ")
print("Second Line")
print("Third Line")