# التكليف 03

#     لديك قاموس يحتوي على المواد العلمية الخاصة بك وال Rank الذي حصلت عليه
#     كل قيمة من القيم في ال Rank تساوي نقاط معينة
#     ال A تساوي 100 وال B تساوي 80 وال C تساوي 40
#     قم بإستخدام ما تعلمته سابقا لتخرج بالنتيجة التالية بدون التعديل على القاموس الأصلي
#     قم بطباعة مجموع النقاط في النهاية بعد إنتهاء ال Loop

# # Input
# my_ranks = {
#   'Math': 'A',
#   "Science": 'B',
#   'Drawing': 'A',
#   'Sports': 'C'
# }

# # Needed Output
# "My Rank in Math Is A And This Equal 100 Points"
# "My Rank in Science Is B And This Equal 80 Points"
# "My Rank in Drawing Is A And This Equal 100 Points"
# "My Rank in Sports Is C And This Equal 40 Points"
# "Total Points Is 320"
# ==========================================

# Input
my_ranks = {
    'Math': 'A',
    "Science": 'B',
    'Drawing': 'A',
    'Sports': 'C'
}

total_point = 0
for key , value in my_ranks.items():
    point = 0
    if value == "A":
        point = 100
    elif value == "B":
        point = 80
    elif value == "C":
        point = 40
    else:
        point = 0
    print(f"My Rank in {key} Is A And This Equal {point} Points")
    total_point += point
else : print(f"Total Points Is {total_point}")
# "My Rank in Math Is A And This Equal 100 Points"
# "My Rank in Science Is B And This Equal 80 Points"
# "My Rank in Drawing Is A And This Equal 100 Points"
# "My Rank in Sports Is C And This Equal 40 Points"
# "Total Points Is 320"
