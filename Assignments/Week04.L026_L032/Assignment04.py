# التكليف 04


#     قم بإنشاء Set تحتوي على العناصر 1, 2, 3
#     قم بإنشاء Set ثانية تحتوي على 1, 2, 3, 4, 5, 6
#     تأكد ان جميع محتويات ال Set الأولى موجود في الثانية أم لا

# set_one = {1, 2, 3}
# set_two = {1, 2, 3, 4, 5, 6}

# # Needed Output

# True
# =================================

set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}

print(set_one.issubset(set_two))
