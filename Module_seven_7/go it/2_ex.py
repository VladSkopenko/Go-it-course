# Модифікуємо приклад попередньої задачі. Для функції do_setup необхідно передбачити другий параметр, який буде списком залежностей.

# Функція do_setup(args_dict, requires) повинна викликати функцію setup з параметрами зі словника args_dict та параметром install_requires, який набуває значення requires.

# Структура словника для параметра args_dicts має бути наступною

# {
#     "name": "useful",
#     "version": "1",
#     "description": "Very useful code",
#     "url": "http://github.com/dummy_user/useful",
#     "author": "Flying Circus",
#     "author_email": "flyingcircus@example.com",
#     "license": "MIT",
#     "packages": ["useful"],
# }