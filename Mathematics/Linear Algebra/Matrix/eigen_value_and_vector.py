import numpy as np

# initializing a matrix
matrix_a = np.array([[4, 2], 
                   [1, 3]])

# calculating eigen values and eigen vector

eigen_value, eigen_vectors = np.linalg.eig(matrix_a)
print(eigen_value)  # output: [5. 2.]
print(eigen_vectors)  
# output:
    # [[ 0.89442719 -0.70710678]
    #  [ 0.4472136   0.70710678]]