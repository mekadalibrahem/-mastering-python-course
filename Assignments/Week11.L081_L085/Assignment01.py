# التكليف 01

#     إستخدم ال Yield مع ما تعلمته لتقوم بعمل Reverse لل String
#     تأكد بعدها ان ال Loop يعمل بنجاح ويخرج النتيجة المطلوبة

# def reverse_string(my_string):
#   # Your Code Here

# # Reverse The String
# for c in reverse_string("Elzero"):
#   print(c)

# ===========================================================

def reverse_string(my_string):
    index = -1 
    for i in my_string :
        yield my_string[index] 
        index -= 1

# Reverse The String
for c in reverse_string("Elzero"):
  print(c)

