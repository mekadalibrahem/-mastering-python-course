'''
====================================
-- 006 - Some Data Types Overviews 
-- link : https://www.youtube.com/watch?v=43lT7k0Zws0&list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs 
====================================
'''
# ----------------------------
# type()
# All Data in Python is Object
# ----------------------------

print(type(10))  # int =&gt; Integer
print(type(100))  # int =&gt; Integer
print(type(-50))  # int =&gt; Integer

print(type(100.9))  # float =&gt; Floating Point Number
print(type(1.950950))  # float =&gt; Floating Point Number
print(type(-100.9595))  # float =&gt; Floating Point Number

print(type("Hello Python"))  # str =&gt; String

print(type([1, 2, 3, 4, 5]))  # list =&gt; List

print(type((1, 2, 3, 4, 5)))  # tuple =&gt; Tuple

print(type({"One": 1, "Two": 2, "Three": 3}))  # dict =&gt; Dictionary

print(type(2 == 2))  # bool =&gt; Boolean