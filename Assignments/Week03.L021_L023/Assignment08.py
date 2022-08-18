# التكليف 08
#  قم بترتيب الأسماء في القائمة في السطر الأول من A إلى Z وفي السطر الثاني من Z إلى A

# friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]

# # Needed Output
# # ['Ahmed', 'Eman', 'Ramy', 'Samah', 'Sayed', 'Shady']
# # ['Shady', 'Sayed', 'Samah', 'Ramy', 'Eman', 'Ahmed']

# ==========================


friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
friends.sort()
print(friends)
friends.sort(reverse = True)
print(friends)