# Generators in Python
# Prerequisites: Yield Keyword and Iterators

# There are two terms involved when we discuss generators.
# 1. Generator-Function : A generator-function is defined like a normal function,
# but whenever it needs to generate a value, it does so with the yield keyword rather than return.
# If the body of a def contains yield, the function automatically becomes a generator function.

# example:

def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3


# Driver code to check above generator function
for value in simpleGeneratorFun():
    print(value)


# 2. Generator-Object : Generator functions return a generator object.
# Generator objects are used either by calling the next method on the generator object or using the generator object
# in a “for in” loop (as shown in the above program).

def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3


# x is a generator object
x = simpleGeneratorFun()

# Iterating over the generator object using next
print(x.__next__())  # In Python 3, __next__() in python 2 x.next()
print(x.__next__())
print(x.__next__())


# So a generator function returns an generator object that is iterable, i.e., can be used as an Iterators .

# Applications : Suppose we to create a stream of Fibonacci numbers,
# adopting the generator approach makes it trivial; we just have to call next(x) to get the next Fibonacci number
# without bothering about where or when the stream of numbers ends.
# A more practical type of stream processing is handling large data files such as log files.
# Generators provide a space efficient method for such data processing as only parts of the file are handled at one
# given point in time. We can also use Iterators for these purposes,
# but Generator provides a quick way (We don’t need to write __next__ and __iter__ methods here).


# The yield statement suspends function’s execution and sends a value back to the caller,
# but retains enough state to enable function to resume where it is left off.
# When resumed, the function continues execution immediately after the last yield run.
# This allows its code to produce a series of values over time,
# rather than computing them at once and sending them back like a list.


# Return sends a specified value back to its caller whereas Yield can produce a sequence of values.
# We should use yield when we want to iterate over a sequence, but don’t want to store the entire sequence in memory.
# Yield are used in Python generators. A generator function is defined like a normal function,
# but whenever it needs to generate a value, it does so with the yield keyword rather than return.
# If the body of a def contains yield, the function automatically becomes a generator function.

def fibonacci():
    current, previous = 0, 1

    while True:
        yield current
        current, previous = current + previous, current


fib = fibonacci()
for i in range(100):
    print(next(fib))
print(__file__)  # current working directory (E:\\python codes\\python practice\\ Generators\\yield_next.py)
