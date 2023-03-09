# An OrderedDict is also a sub-class of dictionary but unlike dictionary,
# it remembers the order in which the keys were inserted.

# OrderedDict preserves the order in which the keys are inserted.
# A regular dict doesn't track the insertion order, and iterating it gives the values in an arbitrary order.
# By contrast, the order the items are inserted is remembered by OrderedDict.

# Syntax:
# class collections.OrderDict()

from collections import OrderedDict

print("This is a Dict:\n")
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

for key, value in d.items():
    print(key, value)

print("\nThis is an Ordered Dict:\n")
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4

for key, value in od.items():
    print(key, value)

# While deleting and re - inserting
# the same key will push the key to the last to maintain the order of insertion of the key.

# Example:

# A Python program to demonstrate working
# of OrderedDict


od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4

print('Before Deleting')
for key, value in od.items():
    print(key, value)

# deleting element
od.pop('a')

# Re-inserting the same
od['a'] = 1

print('\nAfter re-inserting')
for key, value in od.items():
    print(key, value)
