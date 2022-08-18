# التكليف 05
# قم بإضافة إسم من أصدقائك للقائمة في أول القائمة أولا ثم قم بإضافة إسم آخر في نهاية القائمة

# friends = ["Osama", "Ahmed", "Sayed"]

# # Needed Output
# # ["Nasser", "Osama", "Ahmed", "Sayed"]
# # ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]
#  =============================


friends = ["Osama", "Ahmed", "Sayed"]
friends.insert(0, "Nasser")
print(friends)
friends.append("Salem")
print(friends)
