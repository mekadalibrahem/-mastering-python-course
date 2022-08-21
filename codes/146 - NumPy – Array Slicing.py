'''
====================================
-- 146 - NumPy – Array Slicing 
-- link : https://www.youtube.com/watch?v=EJ_TW1qiFI0&list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs 
====================================
'''
# ----------------------------
# -- Numpy =&gt; Array Slicing --
# ----------------------------

import numpy as np

# Slicing =&gt; [Start:End:Steps] Not Including End

a = np.array(["A", "B", "C", "D", "E", "F"])

print(a.ndim)
print(a[1])
print(a[1:4])
print(a[:4])
print(a[2:])

print("#" * 50)

b = np.array([["A", "B", "X"], ["C", "D", "Y"], ["E", "F", "Z"], ["M", "N", "O"]])

print(b.ndim)
print(b[1])

print("#" * 50)

print(b[2:, :2])
print(b[2:, :2:2])