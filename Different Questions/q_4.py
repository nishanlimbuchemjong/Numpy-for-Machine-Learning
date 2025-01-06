"""
Create a 2 X 3 X 4 array and iterate through:
Each element using nditer().
Each row using loops.
"""
import numpy as np

# creating an 2 X 3 X 4 array
arr = np.random.randint(1, 50, size=(2, 3, 4))
print(arr)
# output:
#     [[[26 13 32  6]
#     [38 18 13 39]
#     [19 13 46 45]]

#     [[49 17 41 18]
#     [25 47 32  9]
#     [31 13  3 40]]]

# iterating through each element using nditer()
for i in np.nditer(arr):
    print(i, end=' ')
# output: 18 48 45 19 27 7 27 34 29 2 46 16 34 17 41 22 34 2 34 13 2 25 3 9
print()
# iterating through 2 blocks
for i in range(arr.shape[0]):
    print(f'Row: {i+1}')
    for j in range(arr.shape[1]):
        print(arr[i, j], end=' ')
    print()

# output: 
#     Row: 1
#     [30 45 37 15] [20 14 43  2] [13 16  2 43]
#     Row: 2
#     [45 48 42 46] [18 32  1 47] [17 29  7 43]