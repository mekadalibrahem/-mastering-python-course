# التكليف 02

#     قم بإنشاء Tuple تحتوي على أسماء 3 من أصدقاءك وأول إسم يكون Osama
#     إستخدم خبرتك وما تعلمته سابقا لتغيير أول إسم من Osama إلى Elzero
#     قم بطباعة محتوى ال Tuple في السطر الأول
#     قم بطباعة النوع للتأكد من أنه Tuple وليس نوع بيانات آخر
#     في السطر الثالث قم بطباعة عدد العناصر داخل ال Tuple

# friends = ("Osama", "Ahmed", "Sayed")

# # Needed Output

# # ("Elzero", "Ahmed", "Sayed")
# # <class 'tuple'>
# # 3 Elements
# =======================================================
friends = ("Osama", "Ahmed", "Sayed")

friends = list(friends)
friends[0] = "Elzero"
friends = tuple(friends)
print(friends)
print(type(friends))
print(f"{len(friends)} Elements")