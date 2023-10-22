# Підсписком (sublist) називають список, що є складовою більшого списку. 
# Підсписок може містити один елемент, множину елементів або бути порожнім.

# Наприклад, [1], [2], [3] та [4] є підсписками списку [1, 2, 3, 4]. Список [2, 3] також входить до складу [1, 2, 3, 4], але при цьому список [2, 4]
# не є підсписком [1, 2, 3, 4], оскільки у вихідному списку числа 2 і 4 не є сусідами.

# Порожній список є підсписком будь-якого списку.

# Напишіть функцію all_sub_lists, що повертає список, який містить всі можливі підсписки заданого.

# Наприклад, якщо функції передано аргумент список [1, 2, 3], то функція має повернути наступний список: [[], [1], [2], [3], [1, 2], [2, 3], [1, 2, 3]].


# Функція all_sub_lists повинна повертати щонайменше один список з порожнім підсписком [[]].

def all_sub_lists(data):
    new_sublist = [[]]
    for length in range(1, len(data) + 1):
        for i in range(0, len(data) - length + 1):
            new_sublist.append(data[i: i + length])
    return new_sublist
    