# Розглянемо завдання на перевірку спаму в електронному листі або фільтрацію заборонених слів у повідомленні.
# Нехай функція is_spam_words приймає рядок (параметр text), перевіряє його на вміст заборонених слів зі списку (параметр spam_words), 
#і повертає результат перевірки: True, якщо є хоч одне слово присутнє зі списку, та False, якщо в тексті стоп-слів не виявлено.
# Слова у параметрі text можуть бути у довільному регістрі, а значить функція is_spam_words, при пошуку заборонених слів, регістру незалежна і весь
# текст має зводитися до нижнього регістру. Для спрощення, будемо вважати, що в рядку є тільки одне заборонене слово.
# Передбачити третій параметр функції space_around, який за замовчуванням дорівнює False. 
#Він відповідатиме за те, що функція шукатиме окреме слово чи ні. Слово вважати, що стоїть окремо, якщо ліворуч від слова знаходиться символ пробілу 
#або воно розташоване на початку тексту, а праворуч від слова знаходиться пробіл або символ крапки.
# Наприклад, у тексті ми шукаємо слово "лох". То в слові "Молох" виклик та результат буде наступним:
# print(is_spam_words("Молох", ["лох"]))  # True
# print(is_spam_words("Молох", ["лох"], True))  # False
# Тобто у другому випадку слово не окреме і є частиною іншого.
# У цьому прикладі функція поверне True в обох випадках.
# print(is_spam_words("Ты лох.", ["лох"]))  # True
# print(is_spam_words("Ты лох.", ["лох"], True))  # True
text = "Ты малох"
text_2 = "Ты лох."
spam_words = ["pidor", "kisd", "Лох"]

def is_spam_words(text, spam_words, space_around=False):
    text = text.lower()
    spam = [word.lower() for word in spam_words]

    if space_around:
        for word in spam:
            if word in text:
                index = text.find(word)
                if (index == 0 or not text[index - 1].isalpha()) and \
                        (index + len(word) == len(text) or not text[index + len(word)].isalpha()):
                    return True
        return False
    else:
        return any(word in text for word in spam)
            
        
print(is_spam_words(text,spam_words,True))
        






                

    
