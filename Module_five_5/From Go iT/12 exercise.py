# У шостій задачі ми писали функцію is_spam_words, яка визначала, чи є чи ні стоп-слова у тексті повідомлення.
# Підемо далі та застосуємо функцію sub модуля re для заміни вказаних у списку стоп-слів на деякий шаблон.
# Наприклад, всі "погані" слова замінюватимемо зірочками. 
# Напишіть функцію replace_spam_words, яка приймає рядок (параметр text), перевіряє його на вміст заборонених слів зі списку (параметр spam_words), 
# та повертає результат рядок, але замість заборонених слів, підставлений шаблон з *, причому довжина шаблону дорівнює довжині забороненого слова. 
# Визначити нечутливість до регістру стоп-слів.
import re


def replace_spam_words(text, spam_words):
    for word in spam_words:
        pomenyat = "*" * len(word)
        pattern = re.compile(re.escape(word), re.IGNORECASE)
        text = pattern.sub(pomenyat, text)

    return text


print(replace_spam_words("Privet ti Lox , piDor", ["lox", "pidor",]))


    


    