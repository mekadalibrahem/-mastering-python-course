""" 
#021 – Lists                -> link : https://www.youtube.com/watch?v=EpZH9JozUzA&list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs
#022 – Lists Methods Part 1 -> link : https://www.youtube.com/watch?v=b5cFjJ278Vk&list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs
#023 – Lists Methods Part 2 -> link : https://www.youtube.com/watch?v=pP0QJbJalik&list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs

"""

# #021 – Lists
# -----------------------------
# -- Lists --
# -----------
# [1] List Items Are Enclosed in Square Brackets
# [2] List Are Ordered, To Use Index To Access Item
# [3] List Are Mutable => Add, Delete, Edit
# [4] List Items Is Not Unique
# [5] List Can Have Different Data Types
# -----------------------------

myAwesomeList = ["One", "Two", "One", 1, 100.5, True]

print(myAwesomeList)  # Whole List
print(myAwesomeList[1])  # "Two"
print(myAwesomeList[-1])  # True
print(myAwesomeList[-3])  # 1

print(myAwesomeList[1:4])  # ['Two', 'One', 1]
print(myAwesomeList[:4])  # ['One', 'Two', 'One', 1]
print(myAwesomeList[1:])  # ['Two', 'One', 1, 100.5, True]

print(myAwesomeList[::1])  # ['One', 'Two', 'One', 1, 100.5, True]
print(myAwesomeList[::2])  # ['One', 'One', 100.5]

print(myAwesomeList)
# myAwesomeList[1] = 2
# myAwesomeList[-1] = False
myAwesomeList[0:3] = ["A"]
print(myAwesomeList)


# #022 – Lists Methods Part 1
# -------------------
# -- Lists Methods --
# -------------------

# append()

myFriends = ["Osama", "Ahmed", "Sayed"]
myOldFriends = ["Haytham", "Samah", "Ali"]

myFriends.append("Alaa")
myFriends.append(100)
myFriends.append(150.200)
myFriends.append(True)
myFriends.append(myOldFriends)

print(myFriends)
print(myFriends[2])
print(myFriends[6])
print(myFriends[7])
print(myFriends[7][2])

# extend()

a = [1, 2, 3, 4]
b = ["A", "B", "C"]
c = ["One", "Two"]

a.extend(b)
a.extend(c)

print(a)

# remove()

x = [1, 2, 3, 4, 5, "Osama", True, "Osama", "Osama"]
x.remove("Osama")
print(x)

# sort()

y = [1, 2, 100, 120, -10, 17, 29]
# y = ["A", "Z", "C"]
y.sort(reverse=True)
print(y)

# reverse()

z = [10, 1, 9, 80, 100, "Osama", 100]
z.reverse()
print(z)
#023 – Lists Methods Part 2 
# -------------------
# -- Lists Methods --
# -------------------

# clear()

a = [1, 2, 3, 4]
a.clear()
print(a)

# copy()

b = [1, 2, 3, 4]
c = b.copy()

print(b)  # Main List
print(c)  # Copied List

b.append(5)

print(b)  # Main List
print(c)  # Copied List

# count()

d = [1, 2, 3, 4, 3, 9, 10, 1, 2, 1]
print(d.count(1))

# index()

e = ["Osama", "Ahmed", "Sayed", "Ramy", "Ahmed", "Ramy"]
print(e.index("Ramy"))

# insert()

f = [1, 2, 3, 4, 5, "A", "B"]
f.insert(0, "Test")
f.insert(-1, "Test")

print(f)

# pop()

g = [1, 2, 3, 4, 5, "A", "B"]
print(g.pop(-3))
