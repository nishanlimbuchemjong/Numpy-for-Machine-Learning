# Q) Create a 2D NumPy array of size 3X3 filled with random integers between 1 and 100. Find the sum, mean, and standard deviation of the array.

import numpy as np

np1 = np.array([[3, 4, 5], [1, 2, 3], [5, 6, 7]])

print(np1)

sum_result = np.sum(np1)
print(f"Sum = {sum_result}")    # output: Sum = 36

mean_result = np.mean(np1)  
print(f"Mean = {mean_result}")  # # output: Mean = 4.0      

st_deviation_result = np.std(np1)
print(f"Standard deviation = {st_deviation_result}") # output: Standard deviation = 1.8257418583505538