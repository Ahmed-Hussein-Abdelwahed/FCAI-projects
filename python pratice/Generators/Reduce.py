# The idea behind Python's reduce() is to take an existing function,
# apply it cumulatively to all the items in an iterable, and generate a single final value.
# In general, Python's reduce() is handy for processing iterables without writing explicit for loops.


# The reduce(fun,seq) function is used to apply a particular function passed in its argument to all of the list
# elements mentioned in the sequence passed along.This function is defined in “functools” module.


# Working :

# At first step, first two elements of sequence are picked and the result is obtained.
# Next step is to apply the same function to the previously attained result and the number just succeeding
# the second element and the result is again stored.
# This process continues till no more elements are left in the container.
# The final returned result is returned and printed on console.


import functools  # importing functools for reduce()
import operator  # importing operator for operator functions
import itertools  # importing itertools for accumulate()

list1 = [1, 3, 5, 6, 2]

# using reduce to compute sum of list
print("The sum of the list elements is : ", end="")
print(functools.reduce(lambda a, b: a + b, list1))  # Output: The sum of the list elements is : 17

# using reduce to compute maximum element from list
print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, list1))  # Output: The maximum element of the list is : 6


# Using Operator Functions

# reduce() can also be combined with operator functions to achieve the similar functionality as with lambda functions
# and makes the code more readable.


# importing functools for reduce()  [above]
# importing operator for operator functions  [above]

list2 = [1, 3, 5, 6, 2]

# using reduce to compute sum of list
# using operator functions
print("The sum of the list elements is : ", end="")
print(functools.reduce(operator.add, list2))  # Output: The sum of the list elements is : 17

print("The product of list elements is : ", end="")
print(functools.reduce(operator.mul, list2))  # Output: The product of list elements is : 180

# using reduce to concatenate string
print("The concatenated product is : ", end="")
print(functools.reduce(operator.add, ["geeks", "for", "geeks"]))  # Output: The concatenated product is : geeksforgeeks


# reduce() vs accumulate()
# Both reduce() and accumulate() can be used to calculate the summation of a sequence elements.
# But there are differences in the implementation aspects in both of these.

# reduce() is defined in “functools” module, accumulate() in “itertools” module.
# reduce() stores the intermediate result and only returns the final summation value.
# Whereas, accumulate() returns a iterator containing the intermediate results.
# The last number of the iterator returned is summation value of the list.
# reduce(fun,seq) takes function as 1st and sequence as 2nd argument.
# In contrast accumulate(seq,fun) takes sequence as 1st argument and function as 2nd argument.


# python code to demonstrate summation
# using reduce() and accumulate()

# initializing list
list4 = [1, 3, 4, 10, 4]

# printing summation using accumulate()
print("The summation of list using accumulate is :", end="")
print(list(itertools.accumulate(list4, lambda x, y: x + y)))
# Output: The summation of list using accumulate is :[1, 4, 8, 18, 22]

# printing summation using reduce()
print("The summation of list using reduce is :", end="")
print(functools.reduce(lambda x, y: x + y, list4))  # Output: The summation of list using reduce is :22
