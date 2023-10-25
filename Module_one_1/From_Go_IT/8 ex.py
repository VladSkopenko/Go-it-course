# Змінна length містить довжину, а змінна width — ширину кімнати. Необхідно зробити розрахунок площі кімнати та результат помістити в змінну area.
# Додайте змінну show, в яку помістіть рядок з наступним шаблоном:
# 'With width <значення ширини> and length <значення довжини> of the room, its area is equal to <значення площі>'.

length = 10
witdh = 6
area = length * witdh
show = f"With width {witdh} and length {length} of the room , its area is equal to {area}"
print(show)