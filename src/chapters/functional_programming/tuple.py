from pprint import pprint
from collections import namedtuple

Person = namedtuple("Person", [
    "first_name",
    "last_name",
    "age"
])

my_very_mutable_list = [
    Person("John", "Doe", 30),
    Person("Jane", "Doe", 25),
    Person("Mister", "Roboto", 1000)]

# this transforms a list into a tuple
pprint(tuple(my_very_mutable_list))

# but the list is still mutable...
del my_very_mutable_list[0]
print()
pprint(tuple(my_very_mutable_list))

# but the array is not even needed. just create the tuple directly with (...)!
my_very_immutable_tuple = (
    Person("John", "Doe", 30),
    Person("Jane", "Doe", 25),
    Person("Mister", "Roboto", 1000)
)
print()
pprint(my_very_immutable_tuple)

# and now it is immutable
print()
del my_very_immutable_tuple[0]