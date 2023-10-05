# Ви вже навчилися працювати з рядками глибше і тепер у вас є повний набір інструментів для обробки рядків за допомогою Python.

# За допомогою функції zip, за аналогією прикладу теорії, створіть словник TRANS для транслітерації. Створюйте словник TRANS поза функцією translate

# Напишіть функцію translate, яка проводить транслітерацію кириличного алфавіту на латинську.

# Функція translate:

# приймає на вхід рядок та повертає рядок;
# проводить транслітерацію кириличних символів на латиницю;

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

TRANS = {}

for c , i  in  zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = i
    TRANS[ord(c.upper())] = i.upper()

    
    


def translate(name):
    translated = name.translate(TRANS)
    return translated

print(translate("Привет"))
    
    