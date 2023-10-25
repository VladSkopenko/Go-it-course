# Скласти програму обчислення площі та гіпотенузи прямокутного трикутника,
# якщо відомі його катети (вводяться користувачем)
catet_1 = float(input("Enter the first cathetus: "))
catet_2 = float(input("Enter the second cathetus: "))

area = 0.5 * catet_1 * catet_2
hypotenuse = (catet_1**2 + catet_2**2)**0.5
print(f"With cathetus_1>>{catet_1} and cathetus_2>>{catet_2} area :{area} and hypotenuse:{hypotenuse}")