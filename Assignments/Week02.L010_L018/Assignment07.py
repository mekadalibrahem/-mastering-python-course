# التكليف 07
# قم بوضع علامات @ قبل أي String يتم إعطائك له على ألا يزيد عدد الأحرف عن 20, شاهد المثال لترى الفكرة

# name_one = "Osama"
# name_two = "Osama_Elzero"

# # Needed Output
# # @@@@@@@@@@@@@@@Osama
# # @@@@@@@@Osama_Elzero

# ==============================

name_one = "Osama"
name_two = "Osama_Elzero"

print( name_one.rjust(20, "@"))
print( name_two.rjust(20, "@"))
