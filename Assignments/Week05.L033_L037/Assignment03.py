# التكليف 03

#     قم بإنشاء متغير باسم num_one والقيمة الخاصة به هي رقم 10
#     قم بإنشاء متغير بإسم num_two والقيمة الخاصة به هي رقم 20
#     قم بإنشاء متغير ثالث بإسم num والقيمة الخاصة به هي رقم 20
#     في السطر الأول قم بطباعة نتيجة فحص إذا كان المتغير num أكبر من واحد من المتغيرين الآخريين فقط وليس الإثنين
#     في السطر الثاني قم بطباعة نتيجة فحص إذا كان المتغير num أكبر من المتغيرين الآخريين أم لا

# num_one = 10
# num_two = 20
# num = 20

# # Needed Output

# True
# False
# ==========================================


num_one = 10
num_two = 20
num = 20

print( 
    bool(
        bool(num > num_one and not num > num_two  )  or 
        bool(num > num_two and not num > num_one)
    )
)

print(bool( num > num_one and  num > num_two ))