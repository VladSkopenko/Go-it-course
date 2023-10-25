 # Написати програму розв'язання лінійного рівняння а * х + b = 0 (а≠0). (a і b вводяться користувачем)
a = float(input("Enter number a >>>"))
b = float(input("Enter number b >>>"))
# ax+b=0
if a != 0 :
 result = -b / a
 print(f"Якщо a:{a} and b:{b} then x:{result}")
elif a == 0 :
 print("Неможливо поділити на нуль")

