#Напишіть функцію get_str_date(date), яка перетворюватиме дату з бази даних у форматі ISO '2021-05-27 17:08:34.149Z' у вигляді наступного рядка
# 'Thursday 27 May 2021' - день тижня, число, місяць та рік. Перетворене значення функція повертає під час виклику.

from datetime import datetime
date = '2021-05-27 17:08:34.149Z'
def get_str_date(date):
    date = datetime.strptime(date, f"%Y-%m-%d %H:%M:%S.%f%z")
    date = datetime.strftime(date, f"%A %d %B %Y")
    return date


print(get_str_date(date))