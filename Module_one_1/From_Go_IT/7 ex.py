# На цю мить у нас є три змінні: first_name, last_name та full_name

# Додамо змінну message, яка фактично буде прототипом шаблонного листа користувачеві, який купив квиток. 
#Цю змінну ми сформуємо за допомогою f-рядка. У змінну message ми, за допомогою f-рядка, помістимо рядок наступного змісту:

# "Dear <підставляємо first_name>, we inform you that you have purchased a ticket to travel to the island of Mauritius.
#  Departure June 31 of this year. Have a passport at <підставляємо full_name>. We are looking forward to seeing you!"

first = "Vlad"
last: str = "Skopenko"
full = first + " " + last
message = (f"Dear {first} we inform you that you have purchased a ticket to travel to the island of Mauritius. Departure June 31 of this year \n"
           f"Have a passport at {full}. We are lookibg forward to seeing you!")
print(message)