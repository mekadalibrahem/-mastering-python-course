# التكليف 01

#     قم بطباعة رسالة فيها عدد الأيام ما بين التاريخ التالي “2021, 6, 25” واليوم
#     شاهد المثال لتفهم الفكرة

# # The Date Is "2021, 6, 25"
# # Today Is "2021, 8, 10"

# # Message Will Be
# "Days From 2021-06-25 To 2021-08-10 Is => 46"
# ===========================================================

import datetime

date1 = datetime.datetime(2021, 6, 25)
date2 = datetime.datetime(2021, 8, 10)
date3 = date2 - date1
print(f"Days From {date1.date()} To {date2.date()} Is => {date3.days}")
