import numpy as np
import pandas as pd
from matplotlib.image import imread  # (imread) ==> image read

# import timeit  # if you want to know the execution time for a statement
# print(timeit.timeit(print(10)))

# optimization in numpy is writen in C language so it faster then its equivalent python code in the data science
# or in machine learning
# we can implement nD arrays using numpy

# data types and attributes

a1 = np.array([1, 2, 3])
a2 = np.array([[1, 2.0, 3.3], [4, 5, 6.5]])  # dimension 2 * 3

print(a1.shape)  # get the dimensions of the array
print(a2.dtype)  # data type
print(a2.size)  # size of the array

# create dataframe from a numpy array

df = pd.DataFrame(a2)  # make the numpy array as dataframe
print(df)

# creating numpy arrays

sample_array = np.array([1, 2, 3])
ones = np.ones((2, 3))
zeros = np.zeros((10, 10))

# we pass here the dimensions of the array that contains ones [default data type is float in ones functions]

print(ones.shape)
print(zeros)

arr = np.arange(10)  # as you can specify the step and the start as normal way
arr1 = np.random.randint(0, 10, size=(2, 5))  # generate 2 * 5 array contains integers not exceed value of 10
arr2 = np.random.random(5)  # generate 5 n random numbers as you can pass the size to create nD array of random numbers
arr3 = np.random.rand(2, 3, 4)  # same as random but here you pass n dimensions

# pseudo random numbers
np.random.seed(seed=10)  # if we want to another someone to use the same generated random numbers
arr4 = np.random.random((2, 5))
print(arr4)

# viewing arrays and matrices

a = np.random.randint(15, size=(3, 5))
a1 = np.unique(a)  # to choose unique random numbers from array a
print(a1)

# get the first numbers from the array

print(a[:, :2])

# manipulating arrays
# arithmetic operations

ones = np.ones(5)
a1 = np.array([1, 2, 3, 4, 5])

# in some situations you can need to search Numpy broadcasting to do the arithmetic operations

print('add ', a1 + ones)  # add a1 elements and ones elements together
print('same as add using + sign ', np.add(a1, ones))
print('sub ', a1 - ones)  # subtract a1 elements and ones elements from each other
print('same as subtract using - sign ', np.subtract(a1, ones))
print('multiply ', a1 * ones)  # and so on
print('same as multiplying using + sign ', np.multiply(a1, ones))
print('division ', a1 / ones)
print('same as division using / sign ', np.divide(a1, ones))
print('int division ', a1 // ones)
print('mod ', a1 % ones)
print('same as mod using % sign ', np.remainder(a1, ones))
print('squared elements of a1 elements', np.square(a1))
print('log of a1 elements ', np.log(a1))
print('exponential of a1 elements ', np.exp(a1))

# there are many functions as the previous


# aggregating functions as:
# min() , max(), sum() ,...
# and so on they are already existing in the normal
# and they are existing in the numpy too
# but numpy is faster


# reshaping & transposing
# varName.reshape()
# varName.T

np.random.seed(seed=10)
at = np.random.randint(1, 10, size=(2, 3))
y = np.random.randint(1, 8, size=(2, 4))
print('at ==> ', at)
print('y ==> ', y)

# dot product vs elements wise

arr = np.random.random((3, 5))
arr1 = np.random.random((5, 3))
print(arr.T.shape)  # will be in 5 * 3 as dimensions
print(np.dot(arr, arr1))  # same as matrices multiplication (c * m) (m * n) ==> result will be in (c * n)

# examples

np.random.seed(0)
sales_amount = np.random.randint(20, size=(5, 3))
weekly_sales = pd.DataFrame(sales_amount,
                            index=['Mon', 'Tues', 'Wed', 'Thurs', 'Fri'],
                            columns=['Almond butter', 'Peanut butter', 'Cashew butter'])
prices = np.array([10, 8, 12])
butter_prices = pd.DataFrame(prices.reshape(1, 3),
                             index=['Price'],
                             columns=['Almond butter', 'Peanut butter', 'Cashew butter'])

# now we want to calc the dot product of the the previous dataframes

total_sales = prices.dot(sales_amount.T)
daily_sales = butter_prices.dot(weekly_sales.T)
weekly_sales['Total ($)'] = daily_sales.T
print(weekly_sales)

# comparison operators (comparison operators numpy)

t1 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
t2 = np.array([10, 1, 5, 3, 6, 8, 4, 7])
print('> ', t1 > t2)
print('<', t1 < t2)
print('== ', t1 == t2)
print('>= ', t1 >= t2)
print('<= ', t1 <= t2)

# sorting arrays

np.random.seed(0)
random_array = np.random.randint(10, size=(3, 5))
x = np.sort(random_array)
u = np.argsort(x)  # indices of elements inside the array
print(np.argmin(x, axis=0))
print(np.argmax(x, axis=1))

# practical example ==> turn images into numpy array

# once you turned the images into numbers you can use methods in numpy ar other in the dataframes

panda = imread('panda.png')
car = imread('car_photo.png')
dog = imread('dog_photo.png')
print(panda)
print(panda.size)
print(panda.shape)
print(panda.ndim)

