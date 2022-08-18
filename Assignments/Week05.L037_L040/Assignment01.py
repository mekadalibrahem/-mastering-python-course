# التكليف 01


#     قم بعمل متغير بإسم name يحتوي على ال Input الخاص بإسم الشخص
#     قم بالتأكد من أن أي مسافات قبل وبعد إسم الشخص سوف يتم إزالتها
#     قم بالتأكد من أن إسم الشخص سوف يكون أول حرف Capital وجميع احروف الأخرى Small
#     قم بطباعة الإسم مع رسالة ترحيبية

# # Input
# "     osAmA   "

# # Needed Output

# "Hello Osama, Happy To See You Here."
# ===============================

name = input("Enter Your name pleasse").strip().capitalize()
print(f"Hello {name:} , Happy To See You Here.")
