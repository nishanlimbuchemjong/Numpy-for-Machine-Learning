"""
Create a 3D array of shape 2X3X4. 
Extract:
    All elements from the second "block."
    The second row of every block.
"""
import numpy as np

# creating a random 3D array
arr1 = np.random.randint(1, 100, size = (2, 3, 4))

# printing the ramdom 3D array
print(f"#D Array: {arr1}")

# extracting second block
print(f"\nAfter Extracting second block: \n{arr1[1]}")

# extracting second row of every blocks
print(f"\nAfter Extracting second row of every block: \n{arr1[:,1,:]}")

