# التكليف 02

    # قم بعمل Loop يطبع الأرقام من 1 إلى 20
    # إذا كان الرقم أقل من 10 ضع قبله صفر
    # قم بإستثناء الأرقام 6 و 8 و 12
    # قم بطباعة رسالة تفيد إنتهاء ال Loop بنجاح

# =======================================================

for num in range(1,21):
    if num == 6 or num == 8 or num == 12 :
        continue
    if num <10 :
        print(f"0{num}")
    else:
        print(num)
else:
    print("All Numbers Printed")