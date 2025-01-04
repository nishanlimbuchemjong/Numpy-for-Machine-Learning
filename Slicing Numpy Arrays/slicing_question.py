"""
Q.1) Create a 3D array of shape 2X3X4. 
Extract:
    All elements from the second "block."
    The second row of every block.
"""
print('Question-1:\n')

import numpy as np

# creating a random 3D array
arr1 = np.random.randint(1, 100, size = (2, 3, 4))

# printing the ramdom 3D array
print(f"#D Array: {arr1}")

# extracting second block
print(f"\nAfter Extracting second block: \n{arr1[1]}")

# extracting second row of every blocks
print(f"\nAfter Extracting second row of every block: \n{arr1[:,1,:]}")

print("...............................................\n")
"""
Q.2) Create a 4x4 array of integers from 1 to 16. Slice the array to extract:
The first two rows.
The last two columns.
A sub-matrix of size 2 X 2 from the center.
"""
print('Question-2:\n')

# creating a 4 X 4 array of integers from 1 to 16
arr2 = np.random.randint(1, 16, size=(4, 4))
print(f"4 X 4 array = \n{arr2}")

# printing the first row of an array
print(f"First row of an array, we get\n{arr2[0]}")

# printing the last two columns of an array
print(f"The last two columns of an array, we get\n{arr2[:, -2:]}")

print(f"A sub-matrix of size 2 X 2 from the center, we get\n{arr2[1:3, -3:-1]}")
print("...............................................\n")