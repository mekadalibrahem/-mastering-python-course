# التكليف 04

#     قم بإنشاء Function لتخرج ال Ouput المطلوب
#     قم بكتابة ال Doc String الخاص بال Function
#     قم بكتابة السطر الذي يقوم بطباعة ال Doc String الخاص بال Function

# # Write Function With Help To Get The Output

# print(say_hello_to("Osama")) # "Hello Osama"

# # Write Doc String Line For The Function Here

# # Function Doc String Output
# "parameter(someone) => Person Name"
# "Function To Say Hello To Anyone"
# # =========================================================

# Write Function With Help To Get The Output

def say_hello_to(someone):
    '''
"parameter(someone) => Person Name"
"Function To Say Hello To Anyone"
    '''
    return f"Hello {someone}"


print(say_hello_to("Osama"))  # "Hello Osama"

# Write Doc String Line For The Function Here

print(say_hello_to.__doc__)
# Function Doc String Output
# "parameter(someone) => Person Name"
# "Function To Say Hello To Anyone"
