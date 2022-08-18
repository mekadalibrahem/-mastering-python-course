# التكليف 06
#  قم بحذف أول إسمين من القائمة ثم بعدها في سطر آخر قم بإزالة آخر إسم من القائمة

# friends = ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]

# # Needed Output
# # ["Ahmed", "Sayed", "Salem"]
# # ["Ahmed", "Sayed"]
#  =====================


friends = ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]
friends.pop(0) 
friends.pop(0)
print(friends)
friends.pop(-1)
print(friends)

