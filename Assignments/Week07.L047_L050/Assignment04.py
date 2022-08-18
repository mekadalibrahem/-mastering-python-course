# التكليف 04

#     قم بإنشاء List فارغة سوف تحتوي لاحقا على أسماء أصدقائك وضعها في متغير بإسم my_friends
#     قم بتحديد أقصى عدد للأصدقاء لإضافتهم في القائمة هو 4
#     قم بعمل Input يطلب منك إسم الشخص الذي تريد إضافته للقائمة
#     إذا كان إسم الشخص كاملا عبارة عن حروف كبيرة Uppercase قم برفض الشخص وإظهار رسالة تفيد أن الإسم غير صالح
#     إذا كان الإسم كله حروف صغيرة قم بتحويل أول حرف فقط لحرف كبير ثم قم بإضافته للقائمة
#     بعد إضافة الإسم تطبع معه رسالة تفيد أنك قمت بتحويل أول حرف لحرف كبير
#     يجب طباعة إسم الشخص مع الرسالة الخاصة بالإضافة
#     في حالة قام الشخص بكتابة إسم وأول حرف فيه كبير قم بإضافته مباشرة وإطبع رسالة تفيد الإضافة
#     في حالة تم إضافة الإسم ومازال هناك مكان آخر في القائمة قم بإظهار ال Input ليقوم بإضافة إسم آخر حتى تمتليء القائمة
#     مع كل إضافة قم بكتابة رسالة تفيد كم عدد الأسماء المتبقية في القائمة قبل أن تمتليء
#     كل إسم يتم إضافته يجب أن يتم إزالة المسافات من قبله وبعده إن وجدت

# # Input
# name = "OSAMA"

# # Needed Output
# "Invalid Name"

# # Input
# name = "osama"

# # Needed Output
# "Friend osama Added => 1st Letter Become Capital"
# "Names Left in List Is 3"

# # Input
# name = "Ahmed"

# # Needed Output
# "Friend Ahmed Added"
# "Names Left in List Is 2"


# =================================

my_friends = []

maxCountName = 4
count = 0
while count < maxCountName:
    name = input(
        "Enter your frinds name  pleasse write all in lowercase letters").strip()
    if name.isupper():
        print("Invalid Name")
    else:
        if name.islower():
            name = name.capitalize()
            print(f"Friend {name} Added => 1st Letter Become Capital")
            count += 1
            print(f"Names Left in List Is {maxCountName - count }")
        else:
            print(f"Friend {name} Added ")
            count += 1
            print(f"Names Left in List Is {maxCountName - count }")
