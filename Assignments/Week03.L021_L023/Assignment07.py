# التكليف 07
#  قم بإنشاء قائمتين آخريين فيهم المزيد من الأصدقاء ثم قم بضمهم على أول قائمة لتخرج بالقائمة النهائية فيها جميع الأصدقاء

# friends = ["Ahmed", "Sayed"]
# employees = ["Samah", "Eman"]
# school = ["Ramy", "Shady"]

# # Needed Output
# # ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]

# ==============================

friends = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]

friends.extend(employees)
friends.extend(school)
print(friends)