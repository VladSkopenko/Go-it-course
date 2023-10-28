# Напишіть програму, яка буде виконувати найпростіші математичні операції з числами послідовно, приймаючи від користувача операнди (числа) та оператор.
#
# Умови для цієї задачі
#
# Додаток працює з цілими та дійсними числами.
# Додаток вміє виконувати такі математичні операції:
# ДОДАВАННЯ (+)
# ВІДНІМАННЯ(-)
# МНОЖЕННЯ (*)
# ДІЛЕННЯ (/)
# Програма приймає один операнд або один оператор за один цикл запит-відповідь.
# Всі операції програма виконує в порядку надходження — одну за одною.
# Програма виводить результат обчислень, коли отримує від користувача символ =.
# Додаток закінчує роботу після того, як виведе результат обчислення.
# Користувач по черзі вводить числа та оператори.
# Якщо користувач вводить оператор двічі поспіль, він отримує повідомлення про помилку і може ввести повторно.
# Якщо користувач вводить число двічі поспіль, він отримує повідомлення про помилку і може ввести повторно.
# Додаток коректно опрацьовує ситуацію некоректного введення (exception).
# Початкові змінні:
#
# result = None
# operand = None
# operator = None
# wait_for_number = True
# result — сюди поміщаємо підсумковий результат operand — завжди зберігає поточне число operator —
# рядковий параметр, може містити чотири значення, "+", "-", "*", "/" wait_for_number — прапорець, який вказує,
# що очікують на вводі оператор (operator) або операнд (operand)
#
# Приклад виконання програми:
#
# >>> 3
# >>> +
# >>> 3
# >>> 2
# 2 is not '+' or '-' or '/' or '*'. Try again
# >>> -
# >>> -
# '-' is not a number. Try again.
# >>> 5
# >>> *
# >>> 3
# >>> =
# Result: 3.0
# Тестові послідовності:
#
# Перша: ["10", "+", "5", "6", "/", "3", "-", "a", "2", "*", "6", "= "], результат 18.0
# Друга: ["2", "3", "-", "1", "+", "10", "*", "2", "="], результат 22.0
result = None
operand = None
operator = None
wait_for_number = True
while True:
    try:
        if wait_for_number:
            operand = float(input("Enter  operand>>>"))
            if operand == "=":
                print(result)
                break
            if operator == None:
                result = operand
            elif operator == "+":
                result += operand
            elif operator == "-":
                result -= operand
            elif operator == "/":
                try:
                    result /= operand
                except ZeroDivisionError:
                    print("ZeroDivisionError")
                    continue
            elif operator == "*":
                result *= operand
        wait_for_number = False
    except ValueError:
        print(f"Enter number pls {operand} is not number ")
        continue
    if not wait_for_number:
        operator = input("Enter operator >>>")
        if operator == "=":
            print(result)
            break
        if operator not in "+-*/=":
            print("fuck")
            continue
        wait_for_number = True

