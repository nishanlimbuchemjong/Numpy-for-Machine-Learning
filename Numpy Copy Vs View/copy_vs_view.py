import numpy as np

# Copy Vs View
np1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(np1)  # output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# creating a view
np2 = np1.view()
print(f"Original np1: {np1}")   # output: Original np1: [50  1  2  3  4  5  6  7  8  9 10]
print(f"Original np2: {np2}")   # output: Original np2: [ 0  1  2  3  4  5  6  7  8  9 10]

np1[0] = 50
print(f"change np1: {np1}")   # output: chnage np1: [50  1  2  3  4  5  6  7  8  9 10]
print(f"Original np2: {np2}")   # output: Original np2: [50  1  2  3  4  5  6  7  8  9 10]
# the above output is same because the view is same as copy but it still connected to the original array

# creating a copy
np3 = np1.copy()
print(f"Original np1: {np1}")   # output: Original np1: [50  1  2  3  4  5  6  7  8  9 10]
print(f"Original np3: {np3}")   # output: Original np2: [ 50  1  2  3  4  5  6  7  8  9 10]

np1[0] = 0
print(f"change np1: {np1}")   # output: change np1: [ 0  1  2  3  4  5  6  7  8  9 10]
print(f"Original np3: {np3}")   # output: Original np2: [ 50  1  2  3  4  5  6  7  8  9 10]

# the above output is not same because the copy jsut copy the array but when an update is done then the original does not change

