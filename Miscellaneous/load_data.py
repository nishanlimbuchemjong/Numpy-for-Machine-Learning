import numpy as np

# loading data from file
datas = np.genfromtxt('data.txt', delimiter=',')
print(datas)
"""
output:
[[  1.  13.  21.  11. 196.  75.   4.   3.  34.   6.   7.   8.   0.   1.
    2.   3.   4.   5.]
 [  3.  42.  12.  33. 766.  75.   4.  55.   6.   4.   3.   4.   5.   6.
    7.   0.  11.  12.]
 [  1.  22.  33.  11. 999.  11.   2.   1.  78.   0.   1.   2.   9.   8.
    7.   1.  76.  88.]]

    """