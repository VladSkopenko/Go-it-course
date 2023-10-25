# Знову повернемося до попереднього завдання. Додамо перед обчисленням змінної payment пояснювальний коментар.
# Закоментуйте текст 'Payment for electricity for the current month', щоб код став робочим.

rate = 1.68
nigth = 10
day = 10
# Payment for electricity for the current month
payment = day * rate + nigth * rate / 2
print(payment)