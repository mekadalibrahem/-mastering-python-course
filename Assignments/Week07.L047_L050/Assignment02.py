# التكليف 02

#     قم بإنشاء قائمة فيها خمس من أصدقائك ثم تأكد أن فيهم إسمين على الأقل مكتوبين بحروف صغيرة والباقي أول حرف من الإسم Capital
#     قم بإستخدام While Loop لطباعة الأسماء كلها مع تجاهل الأسماء التي تبدأ بحروف صغيرة
#     قم بطباعة عدد الأسماء التي تم تجاهلها ويجب أن تكون بطريقة برمجية وليست يدوية

# # Input
# friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]

# # Needed Output
# "Mohamed"
# "Shady"
# "Sherif"
# "Friends Printed And Ignored Names Count Is 2"
# =======================================================

friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]


count = 0
countIgnoredNames = 0
while count <= len(friends) - 1:
    if friends[count][0].islower():
        countIgnoredNames += 1

    else:
        print(friends[count])
    count += 1

print(f"Friends Printed And Ignored Names Count Is {countIgnoredNames}")
