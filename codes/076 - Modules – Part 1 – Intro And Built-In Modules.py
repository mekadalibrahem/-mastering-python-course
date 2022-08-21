'''
====================================
-- 076 - Modules – Part 1 – Intro And Built-In Modules 
-- link : https://www.youtube.com/watch?v=z7g9gCYYLiU&list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs 
====================================
'''
# ---------------------------------
# -- Modules =&gt; Built In Modules --
# ---------------------------------
# [1] Module is A File Contain A Set Of Functions
# [2] You Can Import Module in Your App To Help You
# [3] You Can Import Multiple Modules
# [4] You Can Create Your Own Modules
# [5] Modules Saves Your Time
# --------------------------------------------------

# Import Main Module
import random
print(random)
print(f"Print Random Float Number {random.random()}")

# Show All Functions Inside Module
print(dir(random))

# Import One Or Two Functions From Module
from random import randint, random
print(f"Print Random Float {random()}")
print(f"Print Random Integer {randint(100, 900)}")