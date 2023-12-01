# Для копіювання екземпляра класу
# Person із попереднього прикладу реалізуйте функцію copy_class_person.
# Як параметр вона приймає екземпляр класу person, та повертає "поверхневу" копію об'єкта за допомогою функції copy із пакета copy.
import copy


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite


def copy_class_person(person):
    return copy.copy(person)
