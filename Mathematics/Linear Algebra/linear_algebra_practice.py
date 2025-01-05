import numpy as np

a = np.ones((2, 3))
print(a)
# Output:
#     [[1. 1. 1.]
#     [1. 1. 1.]]

b = np.full((3, 2), 2)
print(b)

# output:
    # [[2 2]
    #  [2 2]
    #  [2 2]]

# multiplying the above two array using matrix multiplication
result = np.matmul(a, b)
print(result)
# Output:
#     [[6. 6.]
#     [6. 6.]]


# finding the determinant
determinant = np.linalg.det(result)
    # [[6. 6.]
    # [6. 6.]]
print(determinant)  # output: 0.0