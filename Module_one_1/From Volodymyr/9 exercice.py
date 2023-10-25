# В Інтернет-магазині зроблено 4 покупки: на $34.34, $12.01, $17.42, $4.93.
# Зі скількох доларів і центів складатиметься підсумкова сума.

a = 34.34
b = 12.01
c = 17.42
d = 4.93

result = a + b + c + b
dollar = int(result)
cent = str(result)
cent  = cent[-2:]
print(f"Your payment \n"
      f"{dollar} dollar \n"
      f"{cent} cent")