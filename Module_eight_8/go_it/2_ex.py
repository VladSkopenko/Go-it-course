# Напишіть функцію визначення кількості днів у конкретному місяці.
# Ваша функція повинна приймати два параметри: month - номер місяця у вигляді цілого числа в діапазоні від 1 до 12 і year - рік,
# що складається із чотирьох цифр. Перевірте, чи функція коректно обробляє місяць лютий високосного року.



from datetime import date


def get_days_in_month(month, year):
    if month in [1,3,5,7,8,10,12]:
        return 31
    if month in [4,6,11,9]:
        return 30
    if month == 2 and year % 4 == 0:
        return 29
    else:
        return 28


print(get_days_in_month(2,2024))



