# Дано радіус кола r (вводяться користувачем). Скласти програму знаходження довжини кола та площі кола
radious = float(input("Enter radius cola>>"))
#S = πr2
import math
area =  math.pi * radious ** 2
long = math.pi * (radious + radious)
print(f"area:{area} and long:{long}")