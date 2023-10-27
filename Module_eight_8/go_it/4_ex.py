# Щоб виграти головний приз лотереї, необхідний збіг кількох номерів на лотерейному квитку з числами, що випали випадковим чином
# і в певному діапазоні під час чергового тиражу. Наприклад, необхідно вгадати шість чисел від 1 до 49 чи п'ять чисел від 1 до 36 тощо.
#
# Напишіть функцію, яка випадково підбиратиме набір чисел для лотерейного квитка. Серед цих чисел не має бути дублікатів.
#
# Формат функції get_numbers_ticket(min, max, quantity), де параметри:
#
# min - мінімальне значення діапазону, не може бути менше 1
# max - максимальне значення діапазону, не може бути більше 1000
# quantity - кількість чисел у наборі (має бути min < quantity < max)
# Функція повинна повернути перелік випадкових чисел за зростанням. Якщо порушено умови обмежень на параметри функції, тоді повернути пустий список.


from random import randrange

def get_numbers_ticket(min, max, quantity):
    lst = []
    new_number = None
    if 1 <= min < 1000 and 1 <= max <= 1000 and max > quantity > min:
         while len(lst) != quantity:
            new_number = randrange(min, max)
            if new_number not in lst:
                lst.append(new_number)
            else:
                continue
    else:
        return []
    lst.sort()
    return lst

print(get_numbers_ticket(1,49,5))







