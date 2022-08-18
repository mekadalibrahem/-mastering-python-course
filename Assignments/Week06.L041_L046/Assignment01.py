# التكليف 01

#     قم بعمل متغيرين بإسم num1, num2 ويكونوا Input يحتوي على الرقم الأول والثاني
#     قم بعمل متغير ثالث بإسم operation يكون عبارة عن Input يحتوي على نوع العملية الحسابية
#     قم بالتأكد من أن متغيرات الأرقام عبارة عن Integer ولا يوجد مسافات قبلهم ولا بعدهم
#     قم بالتأكد أن المتغير الخاص بالعملية الحسابية لا توجد مسافات قبله ولا بعده
#     قم بجلب الرقم الأول والثاني والعملية الحسابية من المدخلات ثم قم بالعملية بناء على الأرقام والعملية الحسابية سواء كانت + – * / %

# # Inputs

# num1 = 20
# num2 = 40
# operation = "+" Or "-" Or "*" Or "/" Or "%"

# Needed Output

# [num1 20] [operation +] [num2]
# Example One 20 + 40 = 60
# Example Two 20 * 40
# ===============================



num1 = int(input("enter number 1: ").strip())
num2 = int(input("enter number 1: ").strip())
operation = input("enter operation  you can choose[ + , - , *  ,/ , % ]: ").strip()

if operation ==  "+" :
    print(f"{num1} + {num2} = {num1 + num2}")
elif operation ==  "-" :
    print(f"{num1} - {num2} = {num1 - num2}")
elif operation ==  "*" :
    print(f"{num1} * {num2} = {num1 * num2}")
elif operation ==  "/" :
    if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    else :
        print("You can\'t  [/] for zero")
elif operation ==  "%" :
    if num2 != 0:
        print(f"{num1} % {num2} = {num1 % num2}")
    else :
        print("You can\'t  [%] for zero")
else:
    print(f"the operation {operation} is invalid ")