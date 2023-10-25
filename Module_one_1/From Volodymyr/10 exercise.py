# Для кава-брейків на конференції закуплено:
# х круасанів, у стаканчиків, z упаковок кави.
# Ціна круасана $1.04, ціна стаканчика - $0.34, ціна упаковки кави $4.42
# Скласти програму, яка обчислює,
# скільки повних доларів пішло на закупівлю їжі для кава-брейків, і яка її вартість у центах.
crou = int(input("Enter crou>>"))
cuple = int(input("Enter cuple>>"))
up_ka = int(input("Enter up_ka>>"))
cost_crou = 1.04
cost_cuple = 0.34
cost_up = 4.42

result = crou * cost_crou + cuple * cost_cuple + up_ka * cost_up
dollar = int(result)
cent = result * 100
cent = cent % 100
print(f"Spend on conference {dollar} dollar \n"
      f"and {cent} if in the cent")