# Підсумкове завдання модуля два було на обчислення арифметичного виразу.
# У задачі на повторення ми підемо трохи іншим шляхом і виконаємо схоже завдання, одночасно закріпивши знання роботи зі рядками та списками.
# Розбиття рядка на лексеми є процес перетворення вихідного рядка в список з підрядків, званих лексемами (token).

# В арифметичному виразі лексемами є: оператори, числа та дужки.
# Операторами у нас будуть такі символи: *, /, - та +.
# Оператори та дужки легко виділити у рядку — вони складаються з одного символу і ніколи не є частиною інших лексем.
# Числа виділити складніше, оскільки ці лексеми можуть складатися з кількох символів. Тому будь-яка безперервна послідовність цифр — це одна числова лексема.

# Напишіть функцію, яка приймає параметр рядок, що містить математичний вираз, і перетворює його в список лексем.
# Кожна лексема має бути або оператором, або числом, або дужкою.

# Приклад:

# "2+ 34-5 * 3" => ['2', '+', '34', '-', '5', '*', '3']
# З метою спрощення вважаємо, що числа можуть бути тільки цілими, 
# і вхідний рядок завжди міститиме математичний вираз, що складається з дужок, чисел та операторів.

# Зверніть увагу, що лексеми можуть відокремлюватися один від одного різною кількістю прогалин,
# а можуть і не відокремлюватися зовсім. Прогалини не є лексемами та до підсумкового списку потрапити не повинні.
a = "2+ 34-5 * 3"
import re
def token_parser(s):
    s = s.replace(" ","")
    tokens = re.findall(r'[\d]+|[-+*/()]', s)

    return tokens



print(token_parser(a))

    
    