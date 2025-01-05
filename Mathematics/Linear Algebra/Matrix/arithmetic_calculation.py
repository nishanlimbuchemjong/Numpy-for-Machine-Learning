import numpy as np

# initializing the matrices
matrix_a = np.array([[1, 2, 3], [4, 5, 6]])
matrix_b = np.array([[7, 8, 9], [1, 2, 3]])

# calculating the addition of two matrices
addition = np.add(matrix_a, matrix_b)

print(addition)
# Output:
#     [[ 8 10 12]
#     [ 5  7  9]]