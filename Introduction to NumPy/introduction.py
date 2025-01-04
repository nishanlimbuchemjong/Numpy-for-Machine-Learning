"""
In python, a list contains all types of data Types like
    lst = ["Nishan", True, 45, [1, 2, 4, 5  ]]
List consumes a lot of memory

To overcome the problem, we use numpy to deal with this.
"""
# Numpy - Numeric Python
"""
array should be of same data type

ndarray -> n-dimensional array

for using numpy we need to import numpy
>> import numpy as np

"""

import numpy as np

# creating an array
np1 = np.array([0, 1, 2, 3, 5, 6])
print(np1)  # output: [0 1 2 3 5 6]

# creating an array using another method arange()
np2 = np.arange(10)
print(np2)  # output: [0 1 2 3 4 5 6 7 8 9]

# step
np3 = np.arange(0, 10, 2)
print(np3)  # output: [0 2 4 6 8]

# creating an arrays of zeros
np4 = np.arange(10)
print(np4)  # output: [0 1 2 3 4 5 6 7 8 9]

# see the shape of an array; shape is to find the length of an array
length = np1.shape
print(length)   # output: (6,)

# creating mutlidimentsional zeros
np5 = np.zeros((2, 10)) # here, 2 is 2-dimension, and 10 is total numbers of elements
print(np5) 
# output: [[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
            # [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]]

# creating full
np6 = np.full((10), 6)  # here, 10 is the total elements, and 6 is the element that is only '6'
print(np6)  # Output: [6 6 6 6 6 6 6 6 6 6]

# creating multidimensional full
np7 = np.full((2, 10), 6)   # here, 2 is the 2-dimensional, 10 is the toaal no. of elements and 6 is the element that is '6' only
print(np7)
# output:
# [[6 6 6 6 6 6 6 6 6 6]
#  [6 6 6 6 6 6 6 6 6 6]]

# converting python list to numpy (np)
lst = [1, 2, 3, 4, 5, 6]
np8 = np.array(lst) 
print(np8)  # output: [1 2 3 4 5 6]

# Accessing any element in numpy is same as accessing any element in python list
print(np8[0])   # output: 1
print(np8[0:4])   # output: [1 2 3 4]
print(np8[-1])   # output: 6
print(np8[::-1])   # output: [6 5 4 3 2 1]