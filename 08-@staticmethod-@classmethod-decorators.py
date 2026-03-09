# Python program to demonstrate
# use of class method and static method.
from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # a class method to create a Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

    # a static method to check if a Person is adult or not.
    @staticmethod
    def isAdult(age):
        return age > 18


person1 = Person('Tariq', 21)
person2 = Person.fromBirthYear('John', 1996)

print(f"[PERSON 1]: {person1.name}, {person1.age}, Is Adult: {person1.isAdult(person1.age)}")
# [PERSON 1]: Tariq, 21, Is Adult: True

print(f"[PERSON 2]: {person2.name}, {person2.age}, Is Adult: {person2.isAdult(person2.age)}")
# [PERSON 2]: John, 30, Is Adult: True