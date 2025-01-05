import numpy as np

# initializing the matrix
matrix_a = np.array([[1, 2, 5], [4, 4, 6], [2, 8, 1]])

# calculating the inverse matrix
result = np.linalg.inv(matrix_a)

print(result)
# output:
#     [[-0.47826087  0.41304348 -0.08695652]
#     [ 0.08695652 -0.09782609  0.15217391]
#     [ 0.26086957 -0.04347826 -0.04347826]]