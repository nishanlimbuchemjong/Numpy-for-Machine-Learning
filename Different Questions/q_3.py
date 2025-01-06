"""
Generate a 3 X 3 array of random floats between 0 and 1.
Apply np.sin(), np.exp(), and np.log() to the array.
Find the sum of all elements greater than 0.5.

"""

import numpy as np

# generating a 3 X 3 array of random floats between 0 and 1
arr = np.random.rand(3, 3)
print(arr)
# output:
#     [[0.26118833 0.45519717 0.18025607]
#     [0.59194037 0.40387689 0.41958321]
#     [0.93168689 0.93133871 0.28610169]]

# Applying np.sin() function to an array
print(np.sin(arr))  
# output: 
    # [[0.77038867 0.21926706 0.57357132]
    # [0.79861582 0.55971494 0.05749094]
    # [0.21507686 0.6393055  0.81516366]]

# Applying np.exp() function to an array
print(np.exp(arr))
# output:
#     [[1.69683998 1.45682857 2.28141511]
#     [2.14595026 1.12908629 1.80288395]
#     [2.49139848 1.421733   2.03440667]]

# Applying np.log() function to an array
print(np.log(arr))
# output:
#     [[-2.00552257 -1.05661321 -0.26948305]
#     [-0.94883706 -1.58689674 -2.15520419]
#     [-0.35232121 -0.97010577 -2.54636133]]

# finding the sum of all elements greater than 0.5
sum_arr = np.sum(arr[arr>0.5])
print(sum_arr)      # output: 2.8379374994438153