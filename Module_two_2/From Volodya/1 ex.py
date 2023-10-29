# Перевірити чи 3-х значне число паліндром
#  101, 202, 535, etc.
while True:
    a = input("Enter number")
    if len(a) == 3:
        if a[0] == a[2]:
             print(f"{a} is palindrom number")
        else:
             print(f"{a} is not palindrom number")
    else:
        a = input("Enter number")