# التكليف 04

#     قم بعمل Loop على ال Tuple التالية مع طباعة ال Index الخاص بكل عنصر
#     يجب أن يبدأ ال Index من رقم 50
#     إذا وجدت أرقام في ال Tuple قم بتجاهلها
#     تأكد أن البيانات يتم طباعتها بطريقة معكوسة لكن ال Index بطريقة منظمة
#     قم بعمل الحل بطريقتين مختلفتين

# skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")

# # Output
# "50 - JavaScript"
# "52 - Python"
# "53 - PHP"
# "55 - CSS"
# "56 - HTML"
# =========================================================

skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")

list_skills = list(filter((lambda skill: str(skill).isalpha()), skills))
list_skills.reverse()
list_skills_with_counter = enumerate(list_skills, 50)
for counter, skill in list_skills_with_counter:
    print(f"{counter} - {skill}")


print("=" * 20)
# way 2


def filter_numbers(list_items):
    result_list = []
    for item in list_items:
        if str(item).isalpha():

            result_list.append(item)

    return result_list


def counter_list(items, start=0, step=1):
    counter = start
    countered_list = []
    for item in items:
        countered_list.append((counter,  item))
        counter += step
    return countered_list


list_skills2 = filter_numbers(skills)
list_skills2.reverse()
list_skills2__with_counter = counter_list(list_skills2, 50)

for  counter , skill in list_skills2__with_counter:
    print(f"{counter} - {skill}")


print("=" * 20)

