# التكليف 01
#     قم بعمل متغير بإسم num عبارة عن Input يقبل من الشخص رقم معين
#     تأكد أن الرقم نوعه Int وأنه أكبر من 0 وإذا لم يكن أكبر من 0 قم بطباعة رسالة تفيد ذلك
#     بعد إدخال الرقم قم بطباعة الرقم الأصغر منه مباشرة فالأصغر فالأصغر حتى تصل لرقم 1
#     يجب عدم طباعة الرقم نفسه وعدم طباعة رقم 0
#     إذا كانت الأرقام تحتوي على رقم 6 لا تطبعه من ضمن الأرقام
#     بعد الإنتهاء من طباعة الأرقام قم بطباعة رسالة تفيد أن طباعة جميع الأرقام تمت بنجاح مع كتابة كم عدد الأرقام التي تم طباعتها

# # Input
# num = 0

# # Needed Output
# "Number 0 Is Not Larger Than 0"

# # Input
# num = 10

# # Needed Output
# 9
# 8
# 7
# 5
# 4
# 3
# 2
# 1
# "8 Numbers Printed Successfully."


# ===============================


num = int(input("enter number large then 0 ").strip())

if num > 0:
    count = 0
    for i in range(num - 1, 0, -1):
        if i == 6 :
            continue
        else:
            count += 1
            print(i)
    
    print(f"{count} Numbers Printed Successfully.")
    
else:
    print("Number 0 Is Not Larger Than 0")

