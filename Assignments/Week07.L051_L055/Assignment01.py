# التكليف 01

#     لدينا قائمة List من الأرقام
#     نريد عمل Loop عليهم لنستخرج الأرقام التي تقبل القسمة على رقم 5 ويرجع عدد صحيح
#     نريد طباعة ترتيب الأرقام تلقائيا قبل كل رقم فيهم
#     نريد طباعة الارقام من الأكبر للأصغر
#     قم بطباعة رسالة تفيد إنتهاء ال Loop بنجاح

# # Input
# my_nums = [15, 81, 5, 17, 20, 21, 13]

# # Needed Output
# "1 => 20"
# "2 => 15"
# "3 => 5"
# "All Numbers Printed"
# ===============================


my_nums = [15, 81, 5, 17, 20, 21, 13]
my_nums.sort(reverse=True)
counter = 1
for item in my_nums:
    if item % 5 == 0:
        print(f"{counter} => {item}")
else:
    print("All Numbers Printed")
