# التكليف 03

#     قم بعمل Input يقبل منك العمر الخاص بالشخص
#     تأكد أن المدخل عبارة عن Integer
#     المطلوب طباعة عمرك بالشهور والأسابيع والأيام والساعات والدقائق والثواني
#     المطلوب طباعة كل وحدة من وحدات الوقت في سطر منفصل
#     يجب التأكد من أن العمر أكبر من 10 وأقل من 100 وفي حالة غير ذلك إطبع رسالة تفيد أن العمر خارج النطاق.

# # Input Example 38

# # Needed Output
# "Your Age In Months Is 456 Months" # Months Example
# "Your Age In Weeks Is 1824 Weeks" # Weeks Example

# ==========================================

age = int(input("Enter your age  : ").strip() ) 

if age > 10 and age < 100 :
    print(f"{age * 12} Months")
    print(f"{age * 12 * 4} Weeks")
    print(f"{age * 12 * 4 * 30} Days")
    print(f"{age * 12 * 4 * 30 * 24} Hs")
    print(f"{age * 12 * 4 * 30 * 24 * 60} Ms")
    print(f"{age * 12 * 4 * 30 * 24 * 60 * 60} Ss")
    print(f"{age * 12 * 4 * 30 * 24 * 60 * 60 * 1000 } MSs")
else:
    print(f"your age is invalid ")