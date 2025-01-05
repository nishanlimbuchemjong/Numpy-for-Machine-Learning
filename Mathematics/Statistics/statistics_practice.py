import numpy as np

stats = np.array([[1, 2, 3], [4, 5, 6]])

print(stats)
# output:
#     [[1 2 3]
#     [4 5 6]]

# finding minimum value
print(np.min(stats))    # output: 1

# finding maximum value
print(np.max(stats))    # output: 6

# finding minimum value of 1 row and 2 row
print(np.min(stats, axis=1))    # output: [1 4]

# finding maximum value of 1 row and 2nd row
print(np.max(stats, axis=1))    # output: [3 6]

# sum of all elements
print(np.sum(stats))    # output: 21

# sum of all elements of 1st and 2nd row only using axis=0
print(np.sum(stats, axis=0))    # output: [5 7 9]



