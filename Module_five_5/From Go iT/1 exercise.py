#Напишіть функцію real_len, яка підраховує та повертає довжину рядка без наступних керівних символів: [\n, \f, \r, \t, \v]
#
#Для перевірки правильності роботи функції real_len їй будуть передані наступні рядки:
#
#'Alex\nKdfe23\t\f\v.\r'
#'Al\nKdfe23\t\v.\r'
text = "'Alex\nKdfe23\t\f\v.\r'"
def real_len(text):
    clear_text = text.replace("\n","")
    clear_text = text.replace("\f","")
    clear_text = text.replace("\r","")
    clear_text = text.replace("\t","")
    clear_text = text.replace("\v","")
    return len(clear_text)
    

print(real_len(text))