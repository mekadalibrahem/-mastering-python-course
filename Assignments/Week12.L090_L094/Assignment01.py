# التكليف 01

#     لديك ال Code التالي يستقبل منك مدخلات
#     بناء على المدخلات سنظهر بعض رسائل الخطأ

# NUM = input("Add Your Number ")

# # Your Code Here

# إذا قام الشخص بإدخال أكثر من Character واحد تظهر له الرسالة التالية

# IndexError: Only One Character Allowed

# إذا كتب رقم مثلا 9 تظهر له الرسالة التالية فيها الرقم بدون أي مشكلة

# ####################
# The Number Is 9
# ####################

# إذا كتب رقم 0 تظهر له رسالة الخطأ التالية

# ValueError: Number M

# ust Be Larger Than 0


# ===========================================================

try :
    NUM = input("Add Your Number ")
    if NUM == "9" : print("The Number Is 9" )
    elif len(NUM )> 1: raise(IndexError) 
    elif NUM == "0" : raise(ValueError)
    elif NUM.isalpha() : raise()
except IndexError :
    print("IndexError: Only One Character Allowed")
except ValueError:
    print("ValueError: Number Must Be Larger Than 0")
except :
    print("Exception: Only Numbers Allowed")
