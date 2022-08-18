# التكليف 05

#     قم بإنشاء Dictionary يحتوي على ثلاث مهارات برمجية مع النسبة المئوية لمستواك فيهم
#     بدون إستخدام ال Loop قم بطباعة كل مهارة في سطر وبجانبها المستوى المكتوب بالنسبة المئوية
#     قم بإضافة مهارة جديدة لل Dictionary مع النسبة المئوية الخاصة بها ثم قم بطباعتها في السطر الخامس

# # Create Dictionary Here

# # Needed Output

# "HTML Progress Is 90%"
# "CSS Progress Is 80%"
# "Python Progress Is 30%"
# "AI Progress Is 20%"
# =======================================================

my_skills = {
    "one": {
        "name": "HTML",
        "progress": "Progress Is 90%"
    },
    "two": {
        "name": "CSS ",
        "progress": "Progress Is 80% "
    },
    "three": {
        "name": "Python",
        "progress": "Progress Is 30%"
    }
}
print(f"{my_skills['one']['name']} {my_skills['one']['progress']} ")
print(f"{my_skills['two']['name']} {my_skills['two']['progress']} ")
print(f"{my_skills['one']['name']} {my_skills['one']['progress']} ")
new_value = {
    "four": {
        "name": "AI",
        "progress": "Progress Is 20%"
    }
}
my_skills.update(new_value)
# print(my_skills)
print(f"{my_skills['four']['name']} {my_skills['four']['progress']} ")
