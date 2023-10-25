# Скласти програму, яка вводить з клавіатури тризначне число і виводить на екран:
# - суму останньої та передостанньої цифри
# - суму останньої та першої цифри

a = input("Enter 3-x meaning number pls>>>")
if len(a) == 3:
    sum_last_and_num_before_last = int(a[-1]) + int(a[-2])
    sum_last_and_first = int(a[-1]) + int(a[0])
    print(f"last and before last={sum_last_and_num_before_last} and sum last and first={sum_last_and_first} ")