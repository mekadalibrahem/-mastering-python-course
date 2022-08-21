'''
====================================
-- 114 - OOP – Part 12 Getters &amp; Setters 
-- link : https://www.youtube.com/watch?v=vsOcbPE_Ih4&list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs 
====================================
'''
# ------------------------------------------------------
# -- Object Oriented Programming =&gt; Getters &amp; Setters --
# ------------------------------------------------------

class Member:

  def __init__(self, name):

    self.__name = name  # Private

  def say_hello(self):

    return f"Hello {self.__name}"

  def get_name(self):  # Getter

    return self.__name

  def set_name(self, new_name):

    self.__name = new_name

one = Member("Ahmed")

one._Member__name = "Sayed"
print(one._Member__name)

print(one.get_name())
one.set_name('Abbas')
print(one.get_name())