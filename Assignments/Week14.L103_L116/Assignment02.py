# التكليف 02

#     قم بكتابة محتويات ال Class لتظهر النتيجة كما في المثال
#     تأكد أن الشخص يظهر له لقبه بناء على ال Gender كالتالي Mr For Male And Mrs For Female
#     قم بطباعة رسالة العمر كما في المثال عن طريق طرح العمر من رقم 40 وإظهار الرسالة

# class User:
#   # Write Class Content

# user_one = User("Osama", "Mohamed", 38, "Male")
# user_two = User("Eman", "Omar", 25, "Female")

# print(user_one.full_details()) # Hello Mr Osama M. [02] Years To Reach 40
# print(user_two.full_details()) # Hello Mrs Eman O. [15] Years To Reach 40
# ########################################

class User:

  # Write Class Content
    def __init__(self , fname ,lname , age , gender):
        self.fname = fname 
        self.lname = lname 
        self.age = age
        self.gender = gender

    def full_details(self):
        if self.gender == "Male" :

            return f"Hello Mr {self.fname} {self.lname[0]}. [{40-self.age}] Years To Reach 40"
        elif self.gender =="Female" :
            return f"Hello Mrs {self.fname} {self.lname[0]}. [{40-self.age}] Years To Reach 40"
        else:
            return f"Hello  {self.fname} {self.lname[0]}. [{40-self.age}] Years To Reach 40"




user_one = User("Osama", "Mohamed", 38, "Male")
user_two = User("Eman", "Omar", 25, "Female")

print(user_one.full_details()) # Hello Mr Osama M. [02] Years To Reach 40
print(user_two.full_details()) # Hello Mrs Eman O. [15] Years To Reach 40