# UserDict is a dictionary - like container that acts as a wrapper around the dictionary objects.
# This container is used when someone wants to create their own dictionary with some modified or new functionality.


# Syntax:
# class collections.UserDict([initialdata])


# Example:

# Python program to demonstrate userdict


from collections import UserDict


# Creating a Dictionary where
# deletion is not allowed
class MyDict(UserDict):

    # Function to stop deletion
    # from dictionary
    def __del__(self):
        raise RuntimeError("Deletion not allowed")

    # Function to stop pop from
    # dictionary
    def pop(self, s=None):
        raise RuntimeError("Deletion not allowed")

    # Function to stop popitem
    # from Dictionary
    def popitem(self, s=None):
        raise RuntimeError("Deletion not allowed")


# Driver's code
d = MyDict({'a': 1,
            'b': 2,
            'c': 3})

d.pop(1)

# Output:

# Traceback(most recent calllast):
# File "/home/f8db849e4cf1e58177983b2b6023c1a3.py", line 32, in < module >
# d.pop(1)
# File "/home/f8db849e4cf1e58177983b2b6023c1a3.py", line 20, in pop
# raise RuntimeError("Deletion not allowed")

# RuntimeError: Deletion not allowed
# Exception ignored in: < bound method MyDict.__del__of {'a': 1, 'b': 2, 'c': 3} >
# Traceback(most recent call last):
# File "/home/f8db849e4cf1e58177983b2b6023c1a3.py", line 15, in __del__
# RuntimeError: Deletion not allowed
