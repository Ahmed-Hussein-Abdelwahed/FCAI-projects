# A NamedTuple returns a tuple object with names for each position which the ordinary tuples
# lack.For example, consider a tuple names student where the first element represents fname,
# second represents lname and the third element represents the DOB.Suppose for calling fname instead of
# remembering the index position you can actually call the element by using the fname argument,
# then it will be really easy for accessing tuples element.This functionality is provided by the NamedTuple.


# Syntax:
# class collections.namedtuple(typename, field_names)


# Example:

from collections import namedtuple

# Declaring namedtuple()
Student = namedtuple('Student', ['name', 'age', 'DOB'])

# Adding values
S = Student('Nandini', '19', '2541997')

# Access using index
print("The Student age using index is : ", end="")
print(S[1])  # # Output: The Student age using index is: 19

# Access using name
print("The Student name using keyname is : ", end="")
print(S.name)  # Output: The Student name using keyname is: Nandini


# Conversion Operations

# 1. _make(): This function is used to return a namedtuple() from the iterable passed as argument.


# 2. _asdict(): This function returns the OrdereDict() as constructed from the mapped values of namedtuple().



# Example:

# Python code to demonstrate namedtuple() and
# _make(), _asdict()

# Declaring namedtuple()
Student = namedtuple('Student', ['name', 'age', 'DOB'])

# Adding values
S = Student('Nandini', '19', '2541997')

# initializing iterable
li = ['Manjeet', '19', '411997']

# initializing dict
di = {'name': "Nikhil", 'age': 19, 'DOB': '1391997'}

# using _make() to return namedtuple()
print("The namedtuple instance using iterable is  : ")
print(Student._make(li))

# Output: The namedtuple instance using iterable is: Student(name='Manjeet', age='19', DOB='411997')


# using _asdict() to return an OrderedDict()
print("The OrderedDict instance using namedtuple is  : ")
print(S._asdict())

# Output: The OrderedDict instance using namedtuple is:
# OrderedDict([('name', 'Nandini'), ('age', '19'), ('DOB', '2541997')])
