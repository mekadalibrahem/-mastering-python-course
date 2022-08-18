# التكليف 02

#     قم بعمل متغير بإسم age يحتوي على ال Input الخاص بعمر الشخص
#     قم بالتأكد من أن المدخل سوف يكون Integer وليس String
#     إذا كان العمر أصغر من 16 قم بطباعة رسالة تعبر عن أن الموقع يحتوي على مقالات غير مناسبة لسن تحت ال 16
#     إذا كان العمر 16 أو أكثر قم بطباعة رسالة ترحيبية تحتوي على العمر وأن الموقع مناسب للشخص

# # Inputs

# 16 # Input One
# 24 # Input Two

# # Needed Output

# "Hello Your Age Is Under 16, Some Articles Is Not Suitable For You" # If Age < 16
# "Hello Your Age Is {Age_Value_If_Larger_Than_16}, All Articles Is Suitable For You" # If Age Is 16+
# =======================================================

age  = int(input("Enter your Age"))

print("Hello Your Age Is Under 16, Some Articles Is Not Suitable For You" 
if age < 16  
else f"Hello Your Age Is {age}, All Articles Is Suitable For You " )
