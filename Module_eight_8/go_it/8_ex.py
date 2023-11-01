from collections import Counter

a = [
    "85.157.172.253",
    "12.123.124.123",
    "82.157.172.253",
    "3.324.341.3124",
    "85.157.172.253",
    "12.123.172.253",
]
def get_count_visits_from_ip(ips):
    ip_counts = Counter(ips)
    return ip_counts


def get_frequent_visit_from_ip(ips):
    ip_counts = Counter(ips)
    return ip_counts.most_common()[0]




print(get_count_visits_from_ip(a))
print(get_frequent_visit_from_ip(a))

# Є список IP адрес:
#
# IP = [
#     "85.157.172.253",
#     ...
# ]
# Реалізуйте дві функції. Перша get_count_visits_from_ip за допомогою Counter повертатиме словник, де ключ це IP, а значення – кількість входжень у вказаний список.
#
# Приклад:
#
# {
#     '85.157.172.253': 2,
#     ...
# }
# Друга функція get_frequent_visit_from_ip повертає кортеж з найбільш часто уживаним в списку IP і кількістю його появ в списку.
