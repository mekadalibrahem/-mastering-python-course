""" 
#026 – Set                -> link : https://www.youtube.com/watch?v=PSc6QX4Py7k&list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs
#027 – Set Methods Part 1 -> link : https://www.youtube.com/watch?v=N06_D5wWobg&list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs
#028 – Set Methods Part 2 -> link : https://www.youtube.com/watch?v=o8pr--y5vuU&list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs
#029 – Set Methods Part 3 -> link : https://www.youtube.com/watch?v=rs9eebZpcaE&list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs

"""

#026 – Set 
# -----------------------------
# -- Set --
# ---------
# [1] Set Items Are Enclosed in Curly Braces
# [2] Set Items Are Not Ordered And Not Indexed
# [3] Set Indexing and Slicing Cant Be Done
# [4] Set Has Only Immutable Data Types (Numbers, Strings, Tuples) List and Dict Are Not
# [5] Set Items Is Unique
# -----------------------------

# Not Ordered And Not Indexed

mySetOne = {"Osama", "Ahmed", 100}
print(mySetOne)
# print(mySetOne[0])

# Slicing Cant Be Done

mySetTwo = {1, 2, 3, 4, 5, 6}
# print(mySetTwo[0:3])

# Has Only Immutable Data Types

# mySetThree = {"Osama", 100, 100.5, True, [1, 2, 3]} # unhashable type: 'list'
mySetThree = {"Osama", 100, 100.5, True, (1, 2, 3)}

print(mySetThree)

# Items Is Unique

mySetFour = {1, 2, "Osama", "One", "Osama", 1}
print(mySetFour)

#027 – Set Methods Part 1
# -----------------
# -- Set Methods --
# -----------------

# clear()

a = {1, 2, 3}
a.clear()
print(a)

# union()

b = {"One", "Two", "Three"}
c = {"1", "2", "3"}
x = {"Zero", "Cool"}

print(b | c)
print(b.union(c, x))

# add()

d = {1, 2, 3, 4}
d.add(5)
d.add(6)
print(d)

# copy()

e = {1, 2, 3, 4}
f = e.copy()

print(e)
print(f)

e.add(6)

print(e)
print(f)

# remove()

g = {1, 2, 3, 4}
g.remove(1)
# g.remove(7)
print(g)

# discard()

h = {1, 2, 3, 4}
h.discard(1)
h.discard(7)
print(h)

# pop()

i = {"A", True, 1, 2, 3, 4, 5}
print(i.pop())

# update()

j = {1, 2, 3}
k = {1, "A", "B", 2}
j.update(['Html', "Css"])
j.update(k)

print(j)


#028 – Set Methods Part 2
# -----------------
# -- Set Methods --
# -----------------

# difference()

a = {1, 2, 3, 4}
b = {1, 2, 3, "Osama", "Ahmed"}
print(a)
print(a.difference(b))  # a - b
print(a)

print("=" * 40)  # Separator

# difference_update()

c = {1, 2, 3, 4}
d = {1, 2, "Osama", "Ahmed"}
print(c)
c.difference_update(d)  # c - d
print(c)

print("=" * 40)  # Separator

# intersection()

e = {1, 2, 3, 4, "X", "Osama"}
f = {"Osama", "X", 2}
print(e)
print(e.intersection(f))  # e & f
print(e)

print("=" * 40)  # Separator

# intersection_update()

g = {1, 2, 3, 4, "X", "Osama"}
h = {"Osama", "X", 2}
print(g)
g.intersection_update(h)  # g & h
print(g)

print("=" * 40)  # Separator

# symmetric_difference()

i = {1, 2, 3, 4, 5, "X"}
j = {"Osama", "Zero", 1, 2, 4, "X"}
print(i)
print(i.symmetric_difference(j))  # i ^ j
print(i)

print("=" * 40)  # Separator

# symmetric_difference_update()

k = {1, 2, 3, 4, 5, "X"}
l = {"Osama", "Zero", 1, 2, 4, "X"}
print(k)
k.symmetric_difference_update(l)  # k ^ l
print(k)


#029 – Set Methods Part 3

# -----------------
# -- Set Methods --
# -----------------

# issuperset()

a = {1, 2, 3, 4}
b = {1, 2, 3}
c = {1, 2, 3, 4, 5}

print(a.issuperset(b))  # True
print(a.issuperset(c))  # False

print("=" * 50)

# issubset()

d = {1, 2, 3, 4}
e = {1, 2, 3}
f = {1, 2, 3, 4, 5}

print(d.issubset(e))  # False
print(d.issubset(f))  # True

print("=" * 50)

# isdisjoint()

g = {1, 2, 3, 4}
h = {1, 2, 3}
i = {10, 11, 12}

print(g.isdisjoint(h))  # False
print(g.isdisjoint(i))  # True