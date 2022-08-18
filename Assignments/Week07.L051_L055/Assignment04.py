# التكليف 04

# لديك قاموس يحتوي على أسماء الطلبة وكل طالب لديه مجموعة من المواد العلمية ودرجاته فيها
# كل قيمة من القيم في ال Rank تساوي نقاط معينة
# ال A تساوي 100 وال B تساوي 80 وال C تساوي 40 وال D تساوي 20
# قم بإستخدام ما تعلمته سابقا لتخرج بالنتيجة التالية بدون التعديل على القاموس الأصلي
# يجب عليك طباعة المخرجات كما هي بالعلامات بكل شيء
# قم بعمل الحل مرة بطريقة عادية ومرة أخرى بإستخدام ال items()
# Input
# students = {
#   "Ahmed": {
#     "Math": "A",
#     "Science": "D",
#     "Draw": "B",
#     "Sports": "C",
#     "Thinking": "A"
#   },
#   "Sayed": {
#     "Math": "B",
#     "Science": "B",
#     "Draw": "B",
#     "Sports": "D",
#     "Thinking": "A"
#   },
#   "Mahmoud": {
#     "Math": "D",
#     "Science": "A",
#     "Draw": "A",
#     "Sports": "B",
#     "Thinking": "B"
#   }
# }

# # Needed Output
# "------------------------------"
# "-- Student Name => Ahmed"
# "------------------------------"
# "- Math => 100 Points"
# "- Science => 20 Points"
# "- Draw => 80 Points"
# "- Sports => 40 Points"
# "- Thinking => 100 Points"
# "Total Points For Ahmed Is 340"
# "------------------------------"
# "-- Student Name => Sayed"
# "------------------------------"
# "- Math => 80 Points"
# "- Science => 80 Points"
# "- Draw => 80 Points"
# "- Sports => 20 Points"
# "- Thinking => 100 Points"
# "Total Points For Sayed Is 360"
# "------------------------------"
# "-- Student Name => Mahmoud"
# "------------------------------"
# "- Math => 20 Points"
# "- Science => 100 Points"
# "- Draw => 100 Points"
# "- Sports => 80 Points"
# "- Thinking => 80 Points"
# "

# Total Points For Mahmoud Is 380"


# =================================

students = {
    "Ahmed": {
        "Math": "A",
        "Science": "D",
        "Draw": "B",
        "Sports": "C",
        "Thinking": "A"
    },
    "Sayed": {
        "Math": "B",
        "Science": "B",
        "Draw": "B",
        "Sports": "D",
        "Thinking": "A"
    },
    "Mahmoud": {
        "Math": "D",
        "Science": "A",
        "Draw": "A",
        "Sports": "B",
        "Thinking": "B"
    }
}


for key in students:

    print("-" * 30)
    print(f"-- Student Name => {key} ")
    print("-" * 30)
    total_point = 0
    for child_key in students[key]:
        point = 0
        if students[key][child_key] == "A":
            point = 100
        elif students[key][child_key] == "B":
            point = 80
        elif students[key][child_key] == "C":
            point = 40
        elif students[key][child_key] == "D":
            point = 20
        else:
            point = 0
        print(f"My Rank in {child_key} Is A And This Equal {point} Points")
        total_point += point
    else:
        print(f"Total Points Is {total_point}")


# =================== way 2  with item ==========================

# for key , value in students.items() :

#     print("-" * 30 )
#     print(f"-- Student Name => {key} ")
#     print("-" * 30 )
#     total_point = 0
#     for child_key , child_value in  value.items() :
#         point = 0
#         if child_value == "A":
#             point = 100
#         elif child_value == "B":
#             point = 80
#         elif child_value == "C":
#             point = 40
#         elif child_value == "D":
#             point = 20
#         else:
#             point = 0
#         print(f"My Rank in {child_key} Is A And This Equal {point} Points")
#         total_point += point
#     else : print(f"Total Points Is {total_point}")
