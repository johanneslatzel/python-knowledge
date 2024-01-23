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

# what a list comprehension looks like
print("---------------------------------------------------------------")
pprint([x for x in persons if x.age > 29])

# wrapping the list in a tuple
print("---------------------------------------------------------------")
pprint(tuple([x for x in persons if x.age > 29]))

# and now lets get rid of the intermedtiate list
print("---------------------------------------------------------------")
pprint(tuple(x for x in persons if x.age > 29))
print("---------------------------------------------------------------")
