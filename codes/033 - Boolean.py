'''
====================================
-- 033 - Boolean 
-- link : https://www.youtube.com/watch?v=eDmGoHk1Y8k&list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs 
====================================
'''
# -------------
# -- Boolean --
# -------------
# [1] In Programming You Need to Known Your If Your Code Output is True Or False
# [2] Boolean Values Are The Two Constant Objects False + True.
# ---------------------------------------------------------------

name = " "
print(name.isspace())

print("=" * 50)

print(100 &gt; 200)
print(100 &gt; 100)
print(100 &gt; 90)

print("=" * 50)

# True Values

print(bool("Osama"))
print(bool(100))
print(bool(100.95))
print(bool(True))
print(bool([1, 2, 3, 4, 5]))

print("=" * 50)

# False Values

print(bool(0))
print(bool(""))
print(bool(''))
print(bool([]))
print(bool(False))
print(bool(()))
print(bool({}))
print(bool(None))