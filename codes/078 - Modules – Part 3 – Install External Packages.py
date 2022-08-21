'''
====================================
-- 078 - Modules – Part 3 – Install External Packages 
-- link : https://www.youtube.com/watch?v=aA96q7oBdVk&list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs 
====================================
'''
# ------------------------------------------
# -- Modules =&gt; Install External Packages --
# ------------------------------------------
# [1] Module vs Package
# [2] External Packages Downloaded From The Internet
# [3] You Can Install Packages With Python Package Manager PIP
# [4] PIP Install the Package and Its Dependencies
# [5] Modules List "https://docs.python.org/3/py-modindex.html"
# [6] Packages and Modules Directory "https://pypi.org/"
# [7] PIP Manual "https://pip.pypa.io/en/stable/reference/pip_install/"
# ---------------------------------------------------------------------

import termcolor
import pyfiglet

print(dir(pyfiglet))
print(pyfiglet.figlet_format("Elzero"))
print(termcolor.colored("Elzero", color="yellow"))

print(termcolor.colored(pyfiglet.figlet_format("Elzero"), color="yellow"))