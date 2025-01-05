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
# converting the datas into integer from float
print(datas.astype('int32'))
"""
[[  1  13  21  11 196  75   4   3  34   6   7   8   0   1   2   3   4   5]
 [  3  42  12  33 766  75   4  55   6   4   3   4   5   6   7   0  11  12]
 [  1  22  33  11 999  11   2   1  78   0   1   2   9   8   7   1  76  88]]

"""

# Boolean Masking and Advanced Indexing

# finding if the elements are greater than 50
print(datas>50)
"""
[[False False False False  True  True False False False False False False
  False False False False False False]
 [False False False False  True  True False  True False False False False
  False False False False False False]
 [False False False False  True False False False  True False False False
  False False False False  True  True]]

"""

# finding the all elements that is greater than 50
print(datas[datas > 50])    # output: [196.  75. 766.  75.  55. 999.  78.  76.  88.]

# finding all the elements that is greater than 50 and less than 100
print(datas[(datas > 50) & (datas < 100)])  # output: [75. 75. 55. 78. 76. 88.]