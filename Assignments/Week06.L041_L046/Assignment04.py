# التكليف 04
#     لديك قائمة فيها أسماء بلاد عربية وأخرى غير عربية
#     لديك قيمة خصومات مخزنة في متغير باسم discount
#     قم بعمل Input يحتوي على إسم البلد الخاصة بالشخص وقم بتخزينه في متغير بإسم country
#     قم بالتأكد من أن إسم البلد أول حرف فيه Capital ولا توجد مسافات قبله ولا بعده
#     قم بفحص إذا كانت البلد موجودة في قائمة البلاد
#     في حالة كانت موجودة قم بطباعة رسالة تفيد أنه لديك خصم معين ثم قم بحساب الخصم
#     في حالة كانت غير موجودة في البلاد قم بطباعة رسالة تفيد أنه لا توجد خصومات وقم بطباعة المبلغ كما هو
#     قم بتجربة إدخال بلد موجودة مرة وبلد غير موجودة مرة لتتأكد من الحل

# # Input Example One "Egypt"
# # Input Example Two "Ghana"

# country = input("Input Your Country")
# countries = ["Egypt", "Palestine", "Syria", "Yemen", "KSA", "USA", "Bahrain", "England"]
# price = 100
# discount = 30

# # Needed Output
# "Your Country Eligible For Discount And The Price After Discount Is $70" # Egypt Example
# "Your Country Not Eligible For Discount And The Price Is $100" #  Ghana Example
# =================================


country = input("Input Your Country").strip().capitalize()
countries = ["Egypt", "Palestine", "Syria", "Yemen", "KSA", "USA", "Bahrain", "England"]
price = 100
discount = 30

if country in countries :
    print(f"Your Country Eligible For Discount And The Price After Discount Is {price - discount}$")
else:
    print(f"Your Country Not Eligible For Discount And The Price Is {price}$")

