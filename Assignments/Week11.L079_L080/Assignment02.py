# التكليف 02

#     قم بطباعة التاريخ والوقت الخاص باليوم الحالي بأكثر من طريقة
#     شاهد المثال لتفهم الفكرة

# # Today Is "2021, 8, 10"

# "2021-08-10"
# "Aug 10, 2021"
# "10 - Aug - 2021"
# "10 / Aug / 21"
# "10 / August / 2021"
# "Tue, 10 August 2021"
# ########################################

import datetime

nowDate = datetime.datetime.now().date()

print(nowDate)
print(f"{nowDate.strftime('%b %d, %Y ')}")
print(f"{nowDate.strftime('%d - %b - %Y ')}")
print(f"{nowDate.strftime('%d / %b / %y ')}")
print(f"{nowDate.strftime('%d / %B / %Y ')}")
print(f"{nowDate.strftime('%a , %d %B  %Y ')}")
