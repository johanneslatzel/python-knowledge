""" This example creates a namedtuple Person to store information about
    a person. The namedtuple is immutable, so it cannot be changed once
    it is created. The attributes are first_name, last_name, and age.
"""
from pprint import pprint
from collections import namedtuple

Person = namedtuple("Person", [
    "first_name",
    "last_name",
    "age"
])

person1 = Person("John", "Doe", 30)
person2 = Person("Jane", "Doe", 25)

pprint(person1)
print()
pprint(person2)
print()
person1.age = 31