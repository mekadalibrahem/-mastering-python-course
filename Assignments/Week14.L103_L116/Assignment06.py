# التكليف 06

#     لديك 3 Classes كل واحد فيهم يحتوي على Property
#     المطلوب إنشاء Class بإسم Name يرث جميع الخواص الموجودة في ال Classes الثلاثة
#     قم بطباعة المطلوب كما في المثال

# class A:

#   def __init__(self, one):

#     self.one = one

# class B:

#   def __init__(self, two):

#     self.two = two

# class C:

#   def __init__(self, three):

#     self.three = three

# # Write The Class Called "Text" Here

# the_name = Text("El", "ze", "ro")

# print(the_name.show_name())

# # Ouput

# # The Name Is Elzero


# =========================================================


class A:

    def __init__(self, one):

        self.one = one


class B:

    def __init__(self, two):

        self.two = two


class C:

    def __init__(self, three):

        self.three = three

# Write The Class Called "Text" Here


class Text(A, B, C):
    def __init__(self, one, two, three):
        A.__init__(self, one)
        B.__init__(self, two)
        C.__init__(self, three)

    def show_name(self):
        return f"The Name Is {self.one + self.two + self.three} "


# ========================
the_name = Text("El", "ze", "ro")

print(the_name.show_name())

# Ouput

# The Name Is Elzero
