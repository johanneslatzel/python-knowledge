from pprint import pprint
from collections import namedtuple

Person = namedtuple("Person", [
    "first_name",
    "last_name",
    "age"
])

persons = (
    Person("John", "Doe", 30),
    Person("Jane", "Doe", 25),
    Person("Mister", "Roboto", 1000),
    Person("Misses", "Roboto", 9999999),
    Person("Taylor", "Swift", 22),
)

# first print all elements
print("---------------------------------------------------------------")
pprint(persons)

# print the tuple but only elements with age > 29
print("---------------------------------------------------------------")
pprint(filter(lambda person: person.age > 29, persons))

# huh, what is this? well filter returns an iterator, so we need to iterate over it
# or we just convert it to a tuple
print("---------------------------------------------------------------")
pprint(tuple(filter(lambda person: person.age > 29, persons)))
print("---------------------------------------------------------------")
