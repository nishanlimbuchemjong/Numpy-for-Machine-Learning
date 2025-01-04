import numpy as np

# creating 1-D Numpy Array and get shape
np1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(np1)  # output: [ 1  2  3  4  5  6  7  8  9 10 11 12]
print(np1.shape)    # output: (12,)

# creating 2-D array and get shape, (rows/columns)
np2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(np2)
# output:
# [[ 1  2  3  4  5]
#  [ 6  7  8  9 10]]

print(np2.shape)    # output: (2, 5)

# reshape 2-D
np3 = np1.reshape(3, 4)
print(np3)
# output:
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]

print(np3.shape)    # output: (3, 4)


# reshape 3-D
np4 = np1.reshape(2, 3, 2)
print(np4)
# output:
# [[[ 1  2]
#   [ 3  4]
#   [ 5  6]]

#  [[ 7  8]
#   [ 9 10]
#   [11 12]]]

print(np4.shape)    # output: (2, 3, 2)

# flatten to 1-D
np5 = np4.reshape(-1)
print(np5)  # output: [ 1  2  3  4  5  6  7  8  9 10 11 12]
print(np5.shape)    # output: (12,)