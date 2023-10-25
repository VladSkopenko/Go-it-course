# Результат пошуку згенерував n записів (вводиться користувачем).
# Скільки сторінок потрібно для відображення цих записів, якщо на 1 сторінку виводиться 10 записів.
import math
result = int(input("Enter count writeeriv"))
much_artiqle = math.ceil(result / 10)
print(much_artiqle)