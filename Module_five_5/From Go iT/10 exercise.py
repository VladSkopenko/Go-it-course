# Напишіть функцію find_word, яка приймає два параметри: перший text та другий word.
# Функція виконує пошук зазначеного слова word у тексті text за допомогою функції search та повертає словник.


import re


def find_word(text, word):
    object_match = re.search(word,text)
    result_dict = {"result":False,
                   "first_index":None,
                   "last_index":None,
                   "search_string":word,
                   "string":text
                  }

    if object_match:
        result_dict["result"] = True
        start_index , end_index = object_match.span()
        result_dict["first_index"] = start_index
        result_dict["last_index"] = end_index
    return result_dict


print(find_word("Hello world","World"))




    


 