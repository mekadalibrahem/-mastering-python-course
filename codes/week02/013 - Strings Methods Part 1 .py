# ---------------------
# -- Strings Methods --
# ---------------------

# strip() rstrip() lstrip()

a = "    I Love Python    "
print(a.strip())
print(a.rstrip())
print(a.lstrip())

a = "#####I Love Python####"
print(a.strip("#"))
print(a.rstrip("#"))
print(a.lstrip("#"))

a = "@#@#@#I Love Python@#@#@#"
print(a.strip("@#"))
print(a.rstrip("@#"))
print(a.lstrip("@#"))

# title()

b = "I Love 2d Graphics and 3g Technology and python"
print(b.title())

# capitalize()

b = "I Love 2d Graphics and 3g Technology and python"
print(b.capitalize())

# zfill

c, d, e, f = "1", "11", "111", "1111"

print(c)
print(d)
print(e)
print(f)

print(c.zfill(4))
print(d.zfill(4))
print(e.zfill(4))
print(f.zfill(4))

# upper()

g = "osama"

print(g.upper())

# lower()

h = "OSama"

print(h.lower())

""" 

ملاحظات الدرس
خاصية capitalize() تقوم بتحويل أول حرف Capital من ال String واذا كان ال String يحتوي على جملة فيها الكثير من الكلمات فانه يقوم بتحويل اول حرف Capital من أول كلمة فقط وباقي الكلمات كل حروفها تكون Small Letter


#  

link : https://www.youtube.com/watch?v=HmDLsnLgt0M&list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs

"""