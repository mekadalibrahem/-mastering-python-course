# التكليف 03
# قم بعمل متغير name وبداخله القيمة “Elzero” ثم عن طريق ال Indexing + Slicing قم بجلب الحرف الثاني في اول سطر والحرف الثالث في ثاني سطر والحرف الأخير في السطر الثالث, يجب عليك جلب الحرف بطريقة دايناميكية حيث أن الكلمة يمكن أن تتغير, شاهد المثال لترى المطلوب

# name = 'Elzero'

# # Needed Output
# # Second Letter Is "l"
# # Third Letter Is "z"
# # Last Letter Is "o"

# =================================================


name = 'Elzero'

print("Second Letter Is " + name[1]);
print("Third Letter Is " + name[2]);
print("Last Letter Is " + name[-1]);
print("==== way 2 ====");
print("Second Letter Is " + name[1:2]);
print("Third Letter Is " + name[2:3]);
print("Last Letter Is " + name[-1]);


