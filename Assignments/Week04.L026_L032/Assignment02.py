# التكليف 02

# #
#     قم بإنشاء Set جديدة تحتوي على الأرقام 1, 2, 3
#     قم بإنشاء Set جديدة تحتوي على الحروف A, B, C
#     قم بدمج ال Set الأولى والثانية بثلاث طرق مختلفة وإطبع كل طريقة في سطر

# nums = {1, 2, 3}
# letters = {"A", "B", "C"}

# # Needed Output

# # {1, 2, 3, "A", "B", "C"}
# # {1, 2, 3, "A", "B", "C"}
# # {1, 2, 3, "A", "B", "C"}
# =======================================================

nums = {1, 2, 3}
letters = {"A", "B", "C"}

way1 = nums | letters
print(way1)

way2 = nums.union(letters)
print(way2)

nums.update(letters)
print(nums)
