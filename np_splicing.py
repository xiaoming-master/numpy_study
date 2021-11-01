"""
@author:ming
@file:np_splicing.py
@time:2021/10/31
"""

import numpy as np

"""
数组拼接
"""
arr1 = np.arange(12).reshape(3, 4)
arr2 = np.arange(12, 20).reshape(2, 4)
print("arr1:", arr1)
print("arr2:", arr2)

# 数值拼接，列数要相同
arr3 = np.vstack((arr1, arr2))
print("arr3:", arr3)

# 水平拼接，行数要相同
arr4 = np.arange(12, 21).reshape(3, 3)
arr5 = np.hstack((arr4, arr1))
print(arr5)

# 将第1行和第3行交换
arr5[[0, 2], :] = arr5[[2, 0], :]
print(arr5)

# 将第1列与第5列交换
arr5[:, [1, 4]] = arr5[:, [4, 1]]
print(arr5)
