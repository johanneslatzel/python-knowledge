# Functional Programming
This chapter is based on the YouTube series [Functional Programming in Python](https://youtube.com/playlist?list=PLP8GkvaIxJP1z5bu4NX_bFrEInBkAgTMr&si=vlbk8pZFg6QRrqfG) by [Real Python](https://www.youtube.com/@realpython) and [Dear Functional Bros](https://www.youtube.com/watch?v=nuML9SmdbJ4) by [CodeAesthetic](https://www.youtube.com/@CodeAesthetic).
It aims to give a quickoverview to beginners and reference for advanced users.

## Immutable Data Structures
The credo of functional programming is "There shall be no state!". In that spirit a function should not have an inner state or should depend on some sort of state at all. Instead a given function should return the same output every time it is given the same input. It is often useful to therefor protect data (that is used in pipelines of functional code) from changes. Datatypes that cannot be changed after initialization are called immutable.

Python has several basic structures and patterns that can be used. The following table offers a sort of translation of common types or patterns and their immutable counterparts.

| Structure/Pattern 	| Immutable Counterpart 	|
|-------------------	|-----------------------	|
| List              	| tuple                 	|
| Data Class        	| namedtuple            	|
| for loop           	| recursive function     	|

### Named Tuple
```python
--8<-- "src/chapters/functional_programming/named_tuple.py"
```
Output:
```
Person(first_name='John', last_name='Doe', age=30)

Person(first_name='Jane', last_name='Doe', age=25)

Traceback (most recent call last):
  ...
    person1.age = 31
    ^^^^^^^^^^^
AttributeError: can't set attribute
```

### Tuple
```python
--8<-- "src/chapters/functional_programming/tuple.py"
```
Output:
```
(Person(first_name='John', last_name='Doe', age=30),
 Person(first_name='Jane', last_name='Doe', age=25),
 Person(first_name='Mister', last_name='Roboto', age=1000))

(Person(first_name='Jane', last_name='Doe', age=25),
 Person(first_name='Mister', last_name='Roboto', age=1000))

(Person(first_name='John', last_name='Doe', age=30),
 Person(first_name='Jane', last_name='Doe', age=25),
 Person(first_name='Mister', last_name='Roboto', age=1000))
 
Traceback (most recent call last):
  ...
    del my_very_immutable_tuple[0]
        ~~~~~~~~~~~~~~~~~~~~~~~^^^
TypeError: 'tuple' object doesn't support item deletion
```

### Recursive Function
```python
--8<-- "src/chapters/functional_programming/recursive_function.py"
```
Output:
```
---------------------------------------------------------------
Person(first_name='John', last_name='Doe', age=30)
Person(first_name='Jane', last_name='Doe', age=25)
Person(first_name='Mister', last_name='Roboto', age=1000)
---------------------------------------------------------------
Person(first_name='John', last_name='Doe', age=30)
Person(first_name='Jane', last_name='Doe', age=25)
Person(first_name='Mister', last_name='Roboto', age=1000)
---------------------------------------------------------------
Person(first_name='John', last_name='Doe', age=30)
Person(first_name='Jane', last_name='Doe', age=25)
Person(first_name='Mister', last_name='Roboto', age=1000)
---------------------------------------------------------------
first name is John
first name is Jane
first name is Mister
---------------------------------------------------------------
```