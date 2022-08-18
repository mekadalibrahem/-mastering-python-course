# التكليف 03

#     قم بإنشاء Tuple تحتوي على الأرقام من 1 إلى 3
#     قم بإنشاء Tuple تحتوي على الحروف من A إلى C
#     قم بعمل Concatenate لهم في Tuple جديدة وقم بطباعة محتواها في السطر الأول
#     في السطر الثاني قم بحساب عدد العناصر الموجودة داخل ال Tuple الجديدة

# nums = (1, 2, 3)
# letters = ("A", "B", "C")

# # Needed Output

# # nums_and_letters_one = (1, 2, 3, "A", "B", "C")
# # 6 Elements
# ==========================================
nums = (1, 2, 3)
letters = ("A", "B", "C")

chars = nums + letters
print(chars)
print(f"{len(chars)} Elements")
