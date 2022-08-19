#  assignment 02

import traceback
import sqlite3
import os


current_folder = os.path.dirname(os.path.abspath(__file__))
#
db = sqlite3.connect(f"{current_folder}\\alzero.db")

cr = db.cursor()

schema_tabel_user = """ 
CREATE TABLE IF NOT EXISTS user (
    user_id INTEGER  NOT NULL UNIQUE  ,
    user_name TEXT NOT NULL UNIQUE ,
    user_email TEXT NOT NULL UNIQUE,
    user_birthDay TEXT NOT NULL UNIQUE
)
"""

cr.execute(schema_tabel_user)

db.commit()


#  assignment 03
""" 

    أكمل على ما سبق
    قم بإضافة أي بيانات عشوائية ل 5 أشخاص في قاعدة البيانات التي أنشأناها
    شاهد الصورة لتشاهد البيانات المطلوبة
    إذا قمت بعمل Run للملف مرة أخرى بمن المفترض إضافة البيانات مرة أخرى وبسبب ان البيانات Unique سيظهر لك Error
    يجب ان تتأكد أنه عند إضافة البيانات يتجاهل هذا الخطأ


"""

list_user = [
    (2, "Sayed", "20/10/1990",  "Sayed@alzero.org"),
    (1, "Ahmad", "20/10/1980",  "Ahmad@alzero.org"),
    (3, "Gamal", "20/11/1992",  "Gamal@alzero.org"),
    (4, "Ali", "20/12/2000",  "Ali@alzero.org"),
    (5, "Samer", "20/10/1985",  "Samer@alzero.org"),
]


for user in list_user:
    try:
        cr.execute("INSERT INTO user VALUES(? , ? , ? , ?)", user)
    except:
        pass

db.commit()

# assignment 04
""" 

    أكمل على ما سبق
    قم بجلب آخر Row في الجدول
    (5, 'Sameh', '08/11/2000', 's@elzero.org')
"""

cr.execute("SELECT * FROM user order by user_id desc limit 1")
print(cr.fetchone())
db.commit()

# assignment 05
""" 

    أكمل على ما سبق
    لديك Input يطلب منك رقم العضو
    إذا كان الرقم الذي أدخله الشخص موجود في قاعدة البيانات قم بحذف هذا العضو
    بعد الحذف قم بإظهار رسالة انه تم حذف العضو بنجاح
    تحت الرسالة قم بجلب جميع البيانات الأخرى بنفس الترتيب كما في المثال
    إذا لم يكن رقم الشخص موجود قم بإظهار رسالة تفيد أن هذا ال ID غير موجود
    شاهد المثال لتفهم المطلوب

# If Id Is Exists => I Choosed ID 2 In This Example

"User Deleted."
"Show Other Data:"
"ID => 1, Name => Ahmed, Date Of Birth => 20/10/1980, Email => a@elzero.org"
"ID => 3, Name => Gamal, Date Of Birth => 05/10/1991, Email => g@elzero.org"
"ID => 4, Name => Mahmoud, Date Of Birth => 09/10/1987, Email => m@elzero.org"
"ID => 5, Name => Sameh, Date Of Birth => 08/11/2000, Email => s@elzero.org"

# If Id Is Not Exists
"User Not Found."

"""

def delete_user(user_id):
    users_id = []
    users_id.append(user_id)
    try :
        del_user = cr.execute("DELETE FROM user where user_id = (?)" , users_id)
        if(del_user.rowcount):
            db.commit()
            return True
        else :
            raise sqlite3.Error
    except:
        print("User Not Found.")

try:
    user_id_to_deleted = int(input("write user id to delted it : ").strip())
    if delete_user(user_id_to_deleted) == True :
        print("User Deleted")
        cr.execute("SELECT * FROM user")
        list_users = cr.fetchall()
        print("Show Other Data:")
        for user in list_users:
            print(
                f"ID => {user[0]}, Name =>  {user[1]}, Date Of Birth =>  {user[2]}, Email => {user[3]}")

except sqlite3.Error as er:
    print(er)


