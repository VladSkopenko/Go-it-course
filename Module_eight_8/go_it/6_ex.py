from decimal import Decimal, getcontext


def decimal_average(number_list, signs_count):
    getcontext().prec = signs_count
    sum = 0
    for i in number_list:
        sum += Decimal(i)

    return Decimal(sum) / Decimal(len(number_list))


print(decimal_average([3, 5, 77, 23, 0.57], 6 ))


# Створіть функцію decimal_average(number_list, signs_count), яка обчислюватиме середнє арифметичне типу Decimal з кількістю значущих цифр signs_count. Параметр number_list — список чисел
#
# Увага
# Не забувайте приводити всі числа у списку до типу `decimal`
#
# Приклад:
#
# виклик функції decimal_average([3, 5, 77, 23, 0.57], 6) поверне 21.714
# виклик функції decimal_average([31, 55, 177, 2300, 1.57], 9) поверне 512.91400
#



