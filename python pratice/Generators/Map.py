# Python's map() is a built-in function that allows you to process and transform all the items
# in an iterable without using an explicit for loop, a technique commonly known as mapping.
# map() is useful when you need to apply a transformation function to each item in an iterable and transform
# them into a new iterable.

# map()
# function returns a map object(which is an iterator) of the results after applying
# the given function to each item of a given iterable (list, tuple etc.)

# Syntax :
# map(fun, iter)

# Parameters :
# fun : It is a function to which map passes each element of given iterable.
# iter : It is a iterable which is to be mapped.

# NOTE : You can pass one or more iterable to the map() function.

# Returns :
# Returns a list of the results after applying the given function to each item of a given iterable (list, tuple etc.)

# NOTE :
# The returned value from map()
# (map object) then can be passed to functions like list() (to create a list), set() (to create a set).


# example 1

def power_3(n):
    return n ** 3


numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
queb = map(power_3, numbers)
print(list(queb))  # Output: [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]


# example 2
# We can also use lambda expressions with map to achieve above result.


# Double all numbers using map and lambda
numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result))  # Output: [2, 4, 6, 8]


# example 3

# Add two lists using map and lambda
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))  # Output: [5, 7, 9]


# example 4

# List of strings
l = ['sat', 'bat', 'cat', 'mat']

# map() can listify the list of strings individually
test = list(map(list, l))
print(test)  # Output: [['s', 'a', 't'], ['b', 'a', 't'], ['c', 'a', 't'], ['m', 'a', 't']]
