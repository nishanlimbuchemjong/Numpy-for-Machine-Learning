"""
Q.1) Create a 3 X 4 NumPy array with random integers between 1 and 50.

Find its shape, size, and dimensions.
Replace all odd numbers with -1.
"""
import numpy as np

# creating a 3 X 4 array with random integers between 1 and 50
arr = np.random.randint(1, 51, size=(3, 4))
print("Original Array:")
print(arr)
# output:
#     [[25 27 27 10]
#     [23 28 41  4]
#     [30 42  2 28]]

# Finding its shape, size, and dimensions
print(arr.shape)    # output: (3, 4)
print(arr.size)    # output: 12
print(arr.ndim)    # output: 2

# Replacing all odd numbers with (-1)
arr[arr % 2 != 0] = -1
print(arr)
# output:
    # [[48 -1  2  4]
    # [36 -1 -1 28]
    # [-1 -1 12 16]]