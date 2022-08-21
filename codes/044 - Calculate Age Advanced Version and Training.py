'''
====================================
-- 044 - Calculate Age Advanced Version and Training 
-- link : https://www.youtube.com/watch?v=MpO84gVARdE&list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs 
====================================
'''
# -------------------------------------------------
# -- Calculate Age Advanced Version and Training --
# -------------------------------------------------

# Write A Very Beautiful Note
print("#" * 80)
print(" You Can Write The First Letter Or Full Name of The Time Unit ".center(80, '#'))
print("#" * 80)

# Collect Age Data
age = input("Please Write Your Age").strip()

# Collect Time Unit Data
unit = input("Please Choose Time Unit: Months, Weeks, Days ").strip().lower()

# Get Time Units
months = int(age) * 12
weeks = months * 4
days = int(age) * 365

if unit == 'months' or unit == 'm':

  print("You Choosed The Unit Months")
  print(f"You Lived For {months:,} Months.")

elif unit == 'weeks' or unit == 'w':

  print("You Choosed The Unit Weeks")
  print(f"You Lived For {weeks:,} Weeks.")

elif unit == 'days' or unit == 'd':

  print("You Choosed The Unit Days")
  print(f"You Lived For {days:,} Days.")