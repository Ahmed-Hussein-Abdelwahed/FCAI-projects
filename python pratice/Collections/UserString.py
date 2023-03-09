# UserString is a string like container and just like UserDict and UserList it acts as a wrapper around
# string objects.It is used when someone wants to create their own strings with some modified or
# additional functionality.


# Syntax:
# class collections.UserString(seq)


# Example:

# Python program to demonstrate userstring


from collections import UserString


# Creating a Mutable String
class Mystring(UserString):

    # Function to append to
    # string
    def append(self, s):
        self.data += s

    # Function to remove from
    # string
    def remove(self, s):
        self.data = self.data.replace(s, "")


# Driver's code
s1 = Mystring("Geeks")
print("Original String:", s1.data)

# Appending to string
s1.append("s")
print("String After Appending:", s1.data)

# Removing from string
s1.remove("e")
print("String after Removing:", s1.data)

# Output: Original String: Geeks
# String After Appending: Geekss
# String after Removing: Gkss
