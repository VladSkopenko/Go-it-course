from collections import deque

MAX_LEN = 5

lifo = deque(maxlen=MAX_LEN)


def push(element):
    lifo.appendleft(element)


def pop():
    if lifo:
        return lifo.popleft()


# LIFO (англ. last in, first out, "останнім прийшов - першим пішов") - спосіб організації даних
# або іншими словами Стек (Stack). У структурованому лінійному списку, організованому за принципом LIFO,
# елементи можуть додаватися та вибиратися тільки з одного кінця, що називається «вершиною списку».
# Структура LIFO може бути проілюстрована наступним малюнком.
#
# lifo
# За допомогою колекції deque реалізуйте структуру даних LIFO.
# Створіть змінну lifo, що містить колекцію deque.
# Обмежте розмір за допомогою константи MAX_LEN.
# Функція push додає значення element на початок списку lifo.
# Функція pop дістає та повертає перше значення зі списку lifo.