from collections import deque

MAX_LEN = 5

fifo = deque(maxlen=MAX_LEN)


def push(element):
    fifo.append(element)


def pop():
    if fifo:
        return fifo.popleft()


# FIFO (англ. first in, first out - "першим прийшов - першим пішов") - спосіб організації даних
# або іншими словами черга. Цей вислів описує принцип технічної обробки черги чи обслуговування
# конфліктних вимог шляхом впорядкування процесу за принципом: "першим прийшов - першим обслужений"
# (ПППО). Той, хто приходить першим, той і обслуговується першим, хто прийде наступним чекає, поки
# обслуговування першого не буде закінчено, і таке інше.
#
# fifo
# За допомогою колекції deque реалізуйте структуру даних FIFO. Створіть змінну fifo,
# що містить колекцію deque. Обмежте розмір за допомогою константи MAX_LEN.
# Функція push додає значення element до кінця списку fifo.
# Функція pop дістає та повертає перше значення зі списку fifo.