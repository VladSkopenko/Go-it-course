# Повернемося до попереднього завдання та виконаємо зворотне.
# Напишіть рекурсивну функцію encode для кодування списку або рядка.
# Як аргумент функція приймає список ( наприклад ["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z" ]) або рядок (наприклад, "XXXZZXXYYYZZ").
# Функція повинна повернути закодований список елементів (наприклад ["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2])

a = "XXXZZXXYYYZZ"

def encode(data):
    if not data:
        return []

    def encode_helper(index, count):
        if index == len(data) - 1:
            return [data[index], count]

        if data[index] == data[index + 1]:
            return encode_helper(index + 1, count + 1)
        else:
            return [data[index], count] + encode_helper(index + 1, 1)

    return encode_helper(0, 1)



print(encode(a))