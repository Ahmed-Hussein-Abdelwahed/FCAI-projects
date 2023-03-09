# Deque(Doubly Ended Queue) is the optimized list for quicker append and pop operations
# from both sides of the container.It provides O(1) time complexity for append and pop
# operations as compared to list with O(n) time complexity.


# Syntax:
# class collections.deque(list)


# This function takes the list as an argument.

# Example:


from collections import deque

# Declaring deque
queue = deque(['name', 'age', 'DOB'])

print(queue)  # Output: deque(['name', 'age', 'DOB'])

# Inserting Elements Elements in deque can be inserted from both ends.To insert the elements from right append()
# method is used and to insert the elements from the left appendleft() method is used.


# Example:

# Python code to demonstrate working of
# append(), appendleft()


# initializing deque
de = deque([1, 2, 3])

# using append() to insert element at right end
# inserts 4 at the end of deque
de.append(4)

# printing modified deque
print("The deque after appending at right is : ")
print(de)  # Output: The deque after appending at right is: deque([1, 2, 3, 4])

# using appendleft() to insert element at right end
# inserts 6 at the beginning of deque
de.appendleft(6)

# printing modified deque
print("The deque after appending at left is : ")
print(de)  # Output: The deque after appending at left is: deque([6, 1, 2, 3, 4])


# Removing Elements Elements can also be removed from the deque from both the ends.To remove elements from right use
# pop() method and to remove elements from the left use popleft() method.


# Example:

# Python code to demonstrate working of
# pop(), and popleft()


# initializing deque
de = deque([6, 1, 2, 3, 4])

# using pop() to delete element from right end
# deletes 4 from the right end of deque
de.pop()

# printing modified deque
print("The deque after deleting from right is : ")
print(de)  # Output: Output: The deque after deleting from right is: deque([6, 1, 2, 3])

# using popleft() to delete element from left end
# deletes 6 from the left end of deque
de.popleft()

# printing modified deque
print("The deque after deleting from left is : ")
print(de)  # Output: The deque after deleting from left is: deque([1, 2, 3])
