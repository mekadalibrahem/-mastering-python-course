'''
====================================
-- 009 - Escape Sequences Characters 
-- link : https://www.youtube.com/watch?v=cr2Nk2E0f5A&list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs 
====================================
'''
# ----------------------------
# Escape Sequences Characters
# \b =&gt; Back Space
# \newline =&gt; Escape New Line + \
# \\ =&gt; Escape Back Slash
# \' =&gt; Escape Single Quotes
# \" =&gt; Escape Double Quotes
# \n =&gt; Line Feed
# \r =&gt; Carriage Return
# \t =&gt; Horizontal Tab
# \xhh =&gt; Character Hex Value
# ----------------------------

# Back Space
print("Hello\bWorld")  # Will Remove o

# Escape New Line + Back Slash
print("Hello \
I Love \
Python")

# Escape Back Slash
print("I Love Back Slash \\")

# Escape Single Quote
print('I Love Single Quote \'Test\' ')

# Escape Double Quotes
print("I Love Double Quotes \"Test\" ")

# Line Feed
print("Hello World\nSecond Line")

# Carriage Return
print("123456\rAbcde")

# Horizontal Tab
print("Hello\tPython")

# Character Hex Value
print("\x4F\x73")