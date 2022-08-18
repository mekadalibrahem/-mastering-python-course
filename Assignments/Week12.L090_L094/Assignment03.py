# التكليف 03

#     قم بإستعمال ال Type Hinting في ال Function التالية

# def calculate(num1, num2):
#   return num1 + num2

# print(calculate(20, 30))
# ===================================================

def calculate(num1  , num2)-> int:
  return num1 + num2

print(calculate(20, 30))