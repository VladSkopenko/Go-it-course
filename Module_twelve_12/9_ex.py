# Реалізуйте метод __copy__ для класу Person.
#
# Реалізуйте методи __copy__ та __deepcopy__ для класу Contacts.

import copy
import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

    def __copy__(self):
        copy_o = Person(self.name, self.email, self.phone, self.favorite)
        copy_o.name = self.name
        copy_o.email = self.email
        copy_o.phone = self.phone
        copy_o.favorite = self.favorite
        return copy_o


class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.is_unpacking = False
        self.count_save = 0

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
        return content

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes["count_save"] = attributes["count_save"] + 1
        return attributes

    def __setstate__(self, value):
        self.__dict__ = value
        self.is_unpacking = True

    def __copy__(self):
        copy_o = Contacts(self.filename, self.contacts)
        copy_o.filename = self.filename
        copy_o.contacts = self.contacts
        copy_o.is_unpacking = self.is_unpacking
        copy_o.count_save = self.count_save
        return copy_o

    def __deepcopy__(self, memo):
        copy_o = Contacts(self.filename)
        memo[id(self)] = copy_o
        copy_o.filename = self.filename
        copy_o.contacts = copy.deepcopy(self.contacts, memo)
        copy_o.is_unpacking = self.is_unpacking
        copy_o.count_save = self.count_save
        return copy_o
