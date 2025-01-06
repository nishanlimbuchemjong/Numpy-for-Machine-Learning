"""
Q.2) Create an array of 10 evenly spaced numbers between 5 and 15.
    Compute the mean, median, and standard deviation.
"""
import numpy as np

# creating an array of 10 evenly spaced numbers between 5 and 15
arr = np.linspace(5, 15, 10)
print(arr)
# output:
#     [ 5.          6.11111111  7.22222222  8.33333333  9.44444444 10.55555556
#     11.66666667 12.77777778 13.88888889 15.        ]

# finding mean
print(np.mean(arr))     # output: 10.0

# finding median of an array
print(np.median(arr))   # output: 10.0

# finding standard deviation of an array
print(np.std(arr))      # output: 3.191423692521127