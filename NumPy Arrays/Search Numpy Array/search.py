import numpy as np

# search
np1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(np1)  # output: [ 0  1  2  3  4  5  6  7  8  9 10]
# return an index number of a number '3' in np1 array
x = np.where(np1 == 3)
print(x)    # output: (array([3]),)-> this the tuple
print(x[0]) # accesing the 1st item of the above tuple; output: [3]

# return even items
np1 = np.array([0, 12, 2, 32, 4, 5, 6, 7, 8, 9, 10])
y = np.where(np1 % 2 == 0)
print(y)    # output: (array([ 0,  1,  2,  3,  4,  6,  8, 10]),)-> tuple
print(y[0]) # output: [ 0  1  2  3  4  6  8 10]

# the below returns all the even numbers from np1
print(np1[y[0]])    # output: [ 0 12  2 32  4  6  8 10]