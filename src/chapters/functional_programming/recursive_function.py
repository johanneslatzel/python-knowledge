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
    Person("Mister", "Roboto", 1000)
)

# how a for loop might iterative over my_very_immutable_tuple
print("---------------------------------------------------------------")
for i in range(0, len(persons)):
    pprint(persons[i])

# but this is of course not in the spirit of functional programming
# since i is a local variable that represents the state of the loop
# instead use a resursive function


def print_tuple(iterable, index=0):
    # this is a recursion anchor (and also a guard clause, so double-cool!)
    if index < 0 or index >= len(iterable):
        return
    pprint(iterable[index])
    print_tuple(iterable, index + 1)


print("---------------------------------------------------------------")
# now call the recursive function
print_tuple(persons)

# now to take this a step further: the action taken in print_tuple is to use pprint
# this can be abstracted out into a function that takes a function as an argument


def foreach_element(iterable, consumer, index=0):
    if index < 0 or index >= len(iterable):
        return
    consumer(iterable[index])
    foreach_element(iterable, consumer, index + 1)


print("---------------------------------------------------------------")
# also prints the tuple
foreach_element(persons, pprint)

print("---------------------------------------------------------------")
# now lets do something else with the elements of the tuple by passing a different function
foreach_element(persons, lambda person: print(
    "first name is", person.first_name))
print("---------------------------------------------------------------")
