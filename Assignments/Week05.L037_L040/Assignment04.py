# التكليف 04

#     قم بعمل متغير باسم email يحتوي على ال Input الخاص بالبريد الإلكتروني للشخص
#     قم بالتأكد من إزالة المسافات قبل وبعد البريد الإلكتروني
#     قم بالتأكد من أن جميع الحروف سوف تكون صغيرة Lower Letters
#     قم بطباعة رسالة في السطر الأول تحتوي على إسم الشخص فقط الموجود قبل علامة @ مع تحويل أول حرف لحرف كبير Capital
#     قم بطباعة رسالة في السطر الثاني تحتوي على الموقع الموجود عليه البريد الإلكتروني فقط بدون ال Domain
#     في السطر الثالث قم بطباعة ال Top Level Domain الموجود بعد ال "Dot"

# # Inputs

# "Osama@Nn.Sa" # Email

# # Needed Output

# "Your Name Is Osama"
# "Email Service Provider Is nn"
# "Top Level Domain Is sa"



# =================================

email  =  input("enter your email ").strip().lower()

indexAt = email.index("@")
indexDot = email.index(".")




print(f"Your Name Is {email[: indexAt]}")
print(f"Email Service Provider Is {email[indexAt+1:indexDot]}")
print(f"Top Level Domain Is {email[indexDot+1:]}")