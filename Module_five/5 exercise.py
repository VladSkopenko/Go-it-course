# Повернемося до нашого завдання із телефонними номерами. Компанія розширюється та вийшла на ринок Азії. Тепер у списку можуть знаходитись телефони різних країн. Кожна країна має свій телефонний код .

# Компанія працює з наступними країнами

# Країна	Код ISO	Префікс
# Japan	JP	+81
# Singapore	SG	+65
# Taiwan	TW	+886
# Ukraine	UA	+380
# Щоб ми могли коректно виконати рекламну SMS кампанію, необхідно створити для кожної країни свій список телефонних номерів.

# Напишіть функцію get_phone_numbers_for_сountries, яка буде:

# Приймати список телефонних номерів.
# Санітизувати (нормалізувати) отриманий список телефонів клієнтів за допомогою нашої функції sanitize_phone_number.
# Сортувати телефонні номери за вказаними у таблиці країнами.
# Повертати словник зі списками телефонних номерів для кожної країни у такому вигляді:
# {
#     "UA": [<тут список телефонів>],
#     "JP": [<тут список телефонів>],
#     "TW": [<тут список телефонів>],
#     "SG": [<тут список телефонів>]
# }
# Якщо не вдалося порівняти код телефону з відомими, цей телефон повинен бути доданий до списку словника з ключем 'UA'.

def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone


def get_phone_numbers_for_countries(list_phones):
    new_phones_list = []
    for correct_phones in list_phones:
        new_phon =  sanitize_phone_number(correct_phones)
        new_phones_list.append(new_phon)
    country_num = {"UA": [],
                   "JP": [],
                   "TW": [],
                   "SG": []}
    for phoner in new_phones_list:
        if phoner.startswith("81"):
            country_num["JP"].append(phoner)
        elif phoner.startswith("65"):
            country_num["SG"].append(phoner)
        elif phoner.startswith("886"): 
            country_num["TW"].append(phoner)
        elif phoner.startswith("380"): 
            country_num["UA"].append(phoner)
        else:
            country_num["UA"].append(phoner)
    return country_num
    


