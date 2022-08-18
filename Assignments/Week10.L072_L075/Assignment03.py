# التكليف 03

#     قم بإستخدام ما تعلمته لتحسب حاصل ضرب جميع الأرقام الموجودة في القائمة nums
#     يجب عليك أن تعرف ان القائمة يمكن أن تتغير عناصرها لذلك الحل لابد أن يعمل على اي قائمة
#     قم بعمل نفس الحل بواسطة Lambda Function

# nums = [2, 4, 6, 2]

# # Output
# 96
#
# ===================================================

from functools import reduce

def mult(num1 , num2):
    return num1 * num2 


nums = [2, 4, 6, 2]

mult_nums = reduce(mult, nums)

print(mult_nums)
print("=" * 20)
#  with lambda 
mult_nums2 = reduce(( lambda num1 , num2 : num1 * num2), nums)
print(mult_nums2)

# Output
# 96