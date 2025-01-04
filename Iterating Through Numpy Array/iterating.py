import numpy as np

# iterating through 1-D array
np1 = np.array([1, 2, 3, 4, 5, 6, 7, 9, 10])

for x in np1:
    print(x)
# output: 
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 9
# 10

# Iterating through 2-D array
np2 = np.array([[1, 2, 3, 4],[5, 6, 7, 8]])
for x in np2:
    # print(x)    # output: [1 2 3 4]
                        # [5 6 7 8]
    for y in x:
        print(y)
        # output:
        # 1
        # 2
        # 3
        # 4
        # 5
        # 6
        # 7
        # 8

# Iterating through 3-D
np3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(np3)

for x in np3:
    # print(x)
    # output:
        # [[1 2 3]
        # [4 5 6]]
        # [[ 7  8  9]
        # [10 11 12]]
    for y in x:
        # print(y)
        # output:
            # [1 2 3]
            # [4 5 6]
            # [7 8 9]
            # [10 11 12]
        for z in y:
            print(z)
            # output: 
                # 1
                # 2
                # 3
                # 4
                # 5
                # 6
                # 7
                # 8
                # 9
                # 10
                # 11
                # 12

# use of np.nditer() for iterating
for x in np.nditer(np3):
    print(x)
    # output:
        # 1
        # 2
        # 3
        # 4
        # 5
        # 6
        # 7
        # 8
        # 9
        # 10
        # 11
        # 12