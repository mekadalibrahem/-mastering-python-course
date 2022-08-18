# التكليف 03

# لديك الصورة التالية حجمها 1200 العرض في 800 الطول
# جميع الحروف داخل مربعات حجمها واحد
# قم بإستخراج حرف ال L من الصورة
# قم بتحويله للون رمادي كما في الصورة المثال المطلوبة
# قم بحفظ الصورة بجانب الصورة الأصلية
# الطلب الثاني قم بقص الصف الثاني من الحروف كاملة
# قم بعمل Rotate لهم مع تغيير اللون لرمادي مثل المثال الأول
# قم بحفظ الصورة بجانب الصورة الأصلية

# ===================================================
from PIL import Image
import os
import datetime

cFile = os.path.abspath(__file__)
cfolder = os.path.dirname(cFile)

my_image = Image.open(f"{cfolder}\\elzero-pillow.png")
# my_image.show()
with_image = 1200
height_image = 800
size_box_L = (with_image/3, 0, (2 * with_image)/3, height_image/2 - 1)
image_L = my_image.crop(size_box_L)
# image_L.show()
convert_L = image_L.convert("L")
# convert_L.show()
convert_L.save(f"{cfolder}\\image1.jpg")


size_box_tow = (0, height_image/2, with_image, height_image)
image_tow = my_image.crop(size_box_tow)
# image_tow.show()
routate_image_tow = image_tow.rotate(180)
# routate_image_tow.show()
convert_image_tow  = routate_image_tow.convert("L")
# convert_image_tow.show()
convert_image_tow.save(f"{cfolder}\\image_tow.png")


