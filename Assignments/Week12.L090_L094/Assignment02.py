# التكليف 02

#     لديك ال Code التالي يستقبل منك مدخلات
#     المطلوب إستعمال Try, Except, Else لتظهر النتائج كما هو في الأمثلة

# LETTER = input("Add Letter From A to Z")

# # Your Code Here

# إذا كتب أكثر من حرف في ال Input تظهر الرسالة التالية

# "You Must Write One Character Only"

# إذا كتب أي حرف بعيدا عن ال A To Z Capital تظهر له الرسالة التالية

# "The Letter Not In A - Z"

# إذا كتب أي حرف من ال A To Z Capital مثلا D تظهر له الرسالة التالية

# "You Typed D"
# ########################################
try :
    LETTER = input("Add Letter From A to Z")
    if len(LETTER )> 1: raise(IndexError) 
    elif LETTER.islower() : raise(ValueError)
    else:
        print(f"You Typed {LETTER}") 
except IndexError:
    print("You Must Write One Character Only")
except ValueError:
    print("The Letter Not In A - Z")
except :
    print("sa")