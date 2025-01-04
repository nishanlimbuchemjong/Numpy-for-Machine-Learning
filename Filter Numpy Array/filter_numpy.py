import numpy as np

# filtering numpy array with boolean index list
np1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

x = [True, True, False, False, False, True, False, True, True]
print(np1)  # output: [1 2 3 4 5 6 7 8 9]
print(np1[x])    # output: [1 2 6 8 9]

filtered = []
for i in np1:
    if i%2 == 0:
        filtered.append(True)
    else:
        filtered.append(False)

print(np1)  # output: [1 2 3 4 5 6 7 8 9]
print(filtered) # output: [False, True, False, True, False, True, False, True, False]
print(np1[filtered])    # output: [2 4 6 8]

# shortcuts
filtered = np1 % 2 == 0
print(np1)  # output: [1 2 3 4 5 6 7 8 9]
print(filtered) # outut: [False  True False  True False  True False  True False]
print(np1[filtered])    # output: [2 4 6 8]