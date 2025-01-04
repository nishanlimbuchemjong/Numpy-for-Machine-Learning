import numpy as np

# Numpy Universal Function
np1 = np.array([0, -1, 2, -3, 4, -5, 6, 7, 8, 9, 10])
print(np1)  # output: [ 0 -1  2 -3  4 -5  6  7  8  9 10]

# square root of each element
print(np.sqrt(np1))

# output:
# [0.         1.         1.41421356 1.73205081 2.         2.23606798
#  2.44948974 2.64575131 2.82842712 3.         3.16227766]

# absolute value 
print(np.absolute(np1))  # output: [ 0  1  2  3  4  5  6  7  8  9 10]

# exponents
print(np.exp(np1))

# output:
# [1.00000000e+00 3.67879441e-01 7.38905610e+00 4.97870684e-02
#  5.45981500e+01 6.73794700e-03 4.03428793e+02 1.09663316e+03
#  2.98095799e+03 8.10308393e+03 2.20264658e+04]

# min/max
print(np.max(np1))  # output: 10
print(np.min(np1))  # output: -5

# sign either negative or positive
print(np.sign(np1)) # output: [ 0 -1  1 -1  1 -1  1  1  1  1  1]

# Trigonometric: sin, cos, log
print(np.sin(np1))   
# output: 
# [ 0.         -0.84147098  0.90929743 -0.14112001 -0.7568025   0.95892427
#  -0.2794155   0.6569866   0.98935825  0.41211849 -0.54402111]