# Скласти програму, яка отримує із клавіатури чотиризначне
# число і виводить на екран середнє арифметичне його цифр.

a = input("Enter 4-x meaning numbers:")

if len(a) == 4:
    b = (int(a[0]) + int(a[1]) + int(a[2]) + int(a[3]) ) / len(a)
    print(f"Среднее арифметичне {b}")
else:
    print(f"Enter 4-x meaning numbers pls")