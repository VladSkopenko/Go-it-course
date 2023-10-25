# Скласти програму, яка переводить час із секунд, визначаючи повну кількість годин, хвилин і секунд
# (наприклад, час 5000 секунд це 1 година 23 хвилини 20 секунд 5000=1*3600+23*60+20).

second = int(input("Enter second"))
hour = second //  3600
minute = (second - hour * 3600) // 60
secondy = second - hour * 3600 - minute * 60

print(f'Hour={hour}\n'
      f'minute={minute}\n'
      f'secondy={secondy}')