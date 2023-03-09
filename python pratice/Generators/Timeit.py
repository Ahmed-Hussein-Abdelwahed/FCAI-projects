import timeit


# timeit —> Measure execution time of small code snippets.
# This module provides a simple way to time small bits of Python code.
# It has both a Command-Line Interface as well as a callable one.
# It avoids a number of common traps for measuring execution times.

print('first example time = ', timeit.timeit('"-".join(str(n) for n in range(100))', number=10000))

print('second example time = ', timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000))

print('third example time = ', timeit.timeit('"-".join(map(str, range(100)))', number=10000))

a = """for i in range(10):
    print('i = '.format(i))"""

print('fourth example time = ', timeit.timeit(a, number=1000))
