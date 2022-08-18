# التكليف 02

    # قم بعمل ال Function المناسبة التي تخرج جميع المخرجات الموجودة في الأمثلة التالية
    # لدينا بيانات جديدة وهي إسم الشخص
    # البيانات يمكن أن تزيد أو تنقص
    # إذا لم يتم كتابة الإسم لا تظهر السطر الترحيبي الأول
    # إذا لم يكن لديه مهارات قم بإظهار رسالة تفيد أنه لا يوجد لديه Score كما في المثال

# # Test 1
# get_people_scores("Osama", Math=90, Science=80, Language=70)

# # Output
# "Hello Osama This Is Your Score Table:"
# "Math => 90"
# "Science => 80"
# "Language => 70"

# # Test 2
# get_people_scores("Mahmoud", Logic=70, Problems=60)

# # Output
# "Hello Mahmoud This Is Your Score Table:"
# "Logic => 70"
# "Problems => 60"

# # Test 3
# get_people_scores(Logic=70, Problems=60)

# # Output
# "Logic => 70"
# "Problems => 60"

# # Test 4
# get_people_scores("Ahmed")

# # Output
# "Hello Ahmed

#  You Have No Scores To Show"


# ########################################

def get_people_scores( name = False ,  **courses):
    if bool(courses):
        if bool(name) :
            print(f"Hello {name} This Is Your Score Table:")
        
        for courses_name, courses_score in courses.items():
            print(f"{courses_name} => {courses_score}")
    else:
        if bool(name) :
            print(f"Hello {name} You Have No Scores To Show ")
            



# # Test 1
get_people_scores("Osama", Math=90, Science=80, Language=70)

# # Output
# "Hello Osama This Is Your Score Table:"
# "Math => 90"
# "Science => 80"
# "Language => 70"
print("-" * 30)

# # Test 2
get_people_scores("Mahmoud", Logic=70, Problems=60)
print("-" * 30)

# # Output
# "Hello Mahmoud This Is Your Score Table:"
# "Logic => 70"
# "Problems => 60"

# # Test 3
get_people_scores(Logic=70, Problems=60)
print("-" * 30)

# # Output
# "Logic => 70"
# "Problems => 60"

# # Test 4
get_people_scores("Ahmed")
print("-" * 30)


# # Output
# "Hello Ahmed

#  You Have No Scores To Show"

