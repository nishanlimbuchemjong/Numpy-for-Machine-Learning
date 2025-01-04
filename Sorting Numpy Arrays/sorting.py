import numpy as np

# np.sort()
np1 = np.array([5, 3, 1, 2, 0, 30])
print(np1)  # output: [ 5  3  1  2  0 30]
print(np.sort(np1)) # output: [ 0  1  2  3  5 30]

# Alphabetical 
np2 = np.array(['Nishan', 'Limbu', 'Dipa', 'Anu', 'Numa'])
print(np2)  # output: ['Nishan' 'Limbu' 'Dipa' 'Anu' 'Numa']
print(np.sort(np2)) # output: ['Anu' 'Dipa' 'Limbu' 'Nishan' 'Numa']

# Booleans (True/False)
np3 = np.array([True, False, False, False, True, True, False])
print(np3)  # output: [ True False False False  True  True False]
print(np.sort(np3)) # output: [False False False False  True  True  True]

# return a copy not change the original
print(np1)  # output: [ 5  3  1  2  0 30]
print(np.sort(np1)) # output: [ 0  1  2  3  5 30]
print(np1)  # output: [ 5  3  1  2  0 30]


# 2-D
np4 = np.array([[5, 8, 4, 2, 8],[9, 10, 1, 0,6]])
print(np4)  
# output: 
    # [[ 5  8  4  2  8]
    # [ 9 10  1  0  6]]
print(np.sort(np4)) 
# output: 
    # [[ 2  4  5  8  8]
    # [ 0  1  6  9 10]]