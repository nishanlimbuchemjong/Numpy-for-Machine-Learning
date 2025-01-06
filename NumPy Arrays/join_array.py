import numpy as np

"""
Join Array: joining means putting contents of two or more arrays in a single array
"""
# initializing two arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])

# joining two arrays to make it single array using np.concatenate()
arr3 = np.concatenate((arr1, arr2))

print(arr3) # output: 