# An advantage of using filter() over a loop is that it returns a filter object,
# which is an iterator that yields values on demand, promoting a lazy evaluation strategy.
# Returning an iterator makes filter() more memory efficient than an equivalent for loop.

# Application of filter function:
# It is normally used with Lambda functions to separate list, tuple, or sets.


# filter() in python
# The filter() method filters the given sequence with the help of a function that tests each element
# in the sequence to be true or not.

# syntax:
# filter(function, sequence)
# Parameters:
# function: function that tests if each element of a
# sequence true or not.
# sequence: sequence which needs to be filtered, it can
# be sets, lists, tuples, or containers of any iterators.

# Returns:
# returns an iterator that is already filtered.

# # function that filters vowels
def fun(variable):
    letters = ['a', 'e', 'i', 'o', 'u']
    if variable in letters:
        return True
    else:
        return False


# # sequence
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']

# # using filter function
filtered = filter(fun, sequence)

print('The filtered letters are:')
for s in filtered:
    print(s)

# Output:
# The filtered letters are:
# e
# e


# Application:

# # a list contains both even and odd numbers.
seq = [0, 1, 2, 3, 5, 8, 13]

# # result contains odd numbers of the list

result = filter(lambda x: x % 2 != 0, seq)
print(list(result))

# Output:
# [1, 3, 5, 13]

# # result contains even numbers of the list

result = filter(lambda x: x % 2 == 0, seq)
print(list(result))

# Output:
# [0, 2, 8]
