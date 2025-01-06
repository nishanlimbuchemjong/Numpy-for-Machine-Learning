import numpy as np

"""
Join Array: joining means putting contents of two or more arrays in a single array
"""
# For 1-D array:

# initializing two arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])

# joining two arrays to make it single array using np.concatenate()
arr3 = np.concatenate((arr1, arr2))

print(arr3) # output: [ 1  2  3  4  5  6  7  8  9 10]


# For 2-D array:

# initializing two arrays
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[6, 7], [8, 9]])

arr3 = np.concatenate((arr1, arr2), axis=1)
print(arr3) 
# output: 
    # [[1 2 6 7]
    #  [3 4 8 9]]

arr3 = np.concatenate((arr1, arr2), axis=0)
print(arr3) 
# Output:
    # [[1 2]
    #  [3 4]
    #  [6 7]
    #  [8 9]]

# merging two arrays using np.stack()
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])

res = np.stack((arr1, arr2), axis=0)
print(res)
# output:
#     [[ 1  2  3  4  5]
#     [ 6  7  8  9 10]]

# merging two arrays using np.hstack() that means on one row
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])

res = np.hstack((arr1, arr2))
print(res)  # output: [ 1  2  3  4  5  6  7  8  9 10]

# merging two arrays using np.vstack() that means on columns
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])

res = np.vstack((arr1, arr2))
print(res)  
# output: 
    # [[ 1  2  3  4  5]
    # [ 6  7  8  9 10]]