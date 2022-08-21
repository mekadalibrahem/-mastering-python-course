'''
====================================
-- 115 - OOP – Part 13 @Property Decorator 
-- link : https://www.youtube.com/watch?v=UgpyNxNiPRg&list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs 
====================================
'''
# --------------------------------------------------------
# -- Object Oriented Programming =&gt; @Property Decorator --
# --------------------------------------------------------

class Member:

  def __init__(self, name, age):

    self.name = name

    self.age = age

  def say_hello(self):

    return f"Hello {self.name}"

  @property
  def age_in_days(self):

    return self.age * 365

one = Member("Ahmed", 40)

print(one.name)
print(one.age)
print(one.say_hello())
# print(one.age_in_days())

print(one.age_in_days)