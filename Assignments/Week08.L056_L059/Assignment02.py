# التكليف 02
#
#     قم بعمل Function تقوم بعمل عمليات حسابية بإسم addition
#     ال Function تقبل عدد غير معلوم من ال Parameters
#     كل ما عليك هو إيجاد حاصل جمع جميع الأرقام التي يتم تمريرها لل Function
#     إذا كان الرقم 10 من ضمن الأرقام لا تقم بإضافته للعملية الحسابية
#     إذا كان الرقم 5 من ضمن الأرقام قم بطرحه من باقي الأرقام بدلا من جمعه

# # Tests
# print(addition(10, 20, 30, 10, 15)) # 65
# print(addition(10, 20, 30, 10, 15, 5, 100)) # 160
# ########################################

def addition(*numbers):
    result = 0  
    for num in numbers:
        if num == 10 : 
            continue
        elif num == 5 :
            result  -= num 
        else:
            result += num 
    
    return result 

# Tests
print(addition(10, 20, 30, 10, 15)) # 65
print(addition(10, 20, 30, 10, 15, 5, 100)) # 160
