# Є два рядки у різних кодуваннях - "utf-8" та "utf-16". Нам необхідно зрозуміти, чи дорівнюються рядки між собою.

# Реалізуйте функцію is_equal_string(utf8_string, utf16_string), яка повертає True, якщо рядки дорівнюють собі, і False — я


def is_equal_string(utf8_string, utf16_string):
    u8 = utf8_string.decode()
    ut16 =  utf16_string.decode('utf-16')
    if u8.casefold() == ut16.casefold():
        return True
    else:
        return False
      
    