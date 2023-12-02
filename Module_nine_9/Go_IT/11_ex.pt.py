# Для списку numbers підрахувати суму елементів за допомогою функції reduce.
#
# numbers = [3, 4, 6, 9, 34, 12]
# Створіть функцію sum_numbers(numbers), результатом виконання якої буде сума чисел всіх елементів списку numbers.
#
from functools import reduce


def sum_numbers(numbers):
    a = reduce(lambda x, y: x + y, numbers)
    return a
