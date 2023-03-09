# Python Collections Module
# The collection Module in Python provides different types of containers.
# A Container is an object that is used to store different objects and provide a way to access the
# contained objects and iterate over them. Some of the built-in containers are Tuple, List, Dictionary, etc.

# Counters

# The Counter holds the data in an unordered collection, just like hashtable objects.
# The elements here represent the keys and the count as values. It allows you to count the items in an iterable list.
# Arithmetic operations like addition, subtraction, intersection, and union can be easily performed on a Counter


# A counter is a sub-class of the dictionary.
# It is used to keep the count of the elements in an iterable in the form of an unordered dictionary
# where the key represents the element in the iterable and value represents the count of that element in the iterable.

# Note: It is equivalent to bag or multiset of other languages.

# Syntax:
# class collections.Counter([iterable-or-mapping])

# Initializing Counter Objects
# The counter object can be initialized using the counter() function and this function can be called in one of the
# following ways:
# With a sequence of items
# With a dictionary containing keys and counts
# With keyword arguments mapping string names to counts

from collections import Counter

# With sequence of items
print('normal ', Counter(['B', 'B', 'A', 'B', 'C', 'A', 'B', 'B', 'A', 'C']))

# with dictionary
print('with dictionary ', Counter({'A': 3, 'B': 5, 'C': 2}))

# with keyword arguments
print('with keyword arguments ', Counter(A=3, B=5, C=2))
