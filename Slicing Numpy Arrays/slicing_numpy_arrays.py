import numpy as np

# slicing Numpy arrays
np1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# return 2, 3, 4, 5
print(np1[1:5]) # output: [2 3 4 5]

# return form something to the end
print(np1[2:])  # output: [ 3  4  5  6  7  8  9 10]

# return negative slices
print(np1[-3:-1])   # output: [8, 9]

# return with steps; here with step 2 from 1 to 5
print(np1[1:5:2]) # output: [2 4]

# steps on the entire array; step 2
print(np1[::2])  # output: [1 3 5 7 9]



# creating 2-d array
np2 = np.array([[1, 2, 3, 4, 5],[6, 7, 8, 9, 10]])

# full out single item
print(np2[1, 2])    # output: 8

# slice a 2-d array
print(np2[0:3, 1:4])    
# output: 
# [[2 3 4]
#  [7 8 9]]