# A DefaultDict is also a sub-class to dictionary.
# It is used to provide some default values for the key that does not exist and never raises a KeyError.

# Dictionaries are a convenient way to store data for later retrieval by name (key).
# Keys must be unique, immutable objects, and are typically strings. The values in a dictionary can be anything


# Syntax:
# class collections.defaultdict(default_factory)
# default_factory is a function that provides the default value for the dictionary created.
# If this parameter is absent then the KeyError is raised.


# Initializing DefaultDict Objects
# DefaultDict objects can be initialized using DefaultDict() method by passing the data type as an argument.


# Example:

from collections import defaultdict

# Defining the dict
d = defaultdict(int)

L = [1, 2, 3, 4, 2, 4, 1, 2]

# Iterate through the list
# for keeping the count
for i in L:

    # The default value is 0
    # so there is no need to
    # enter the key first
    d[i] += 1

print(d)  # Output: defaultdict(<class 'int'>, {1: 2, 2: 3, 3: 1, 4: 2})


# Example 2:

# Defining a dict
d = defaultdict(list)

for i in range(5):
    d[i].append(i)

print("Dictionary with values as list:")
print(d)

# Output:
# Dictionary with values as list:
# defaultdict(<class ‘list’>, {0: [0], 1: [1], 2: [2], 3: [3], 4: [4]})


# Example 2:

# Defining a dict
d = defaultdict(list)

for i in range(5):
    d[i].append(i)

print("Dictionary with values as list:")
print(d)

# Output:

# Dictionary with values as list:
# defaultdict( <class ‘list’ >, {0: [0], 1: [1], 2: [2], 3: [3], 4: [4]})
