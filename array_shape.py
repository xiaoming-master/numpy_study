"""
@author:ming
@file:array_shape.py
@time:2021/10/29
"""

import numpy as np

"""
数组的形状
    shape=array.shape 获取数组的形状，返回一个元组。对于一个二维数组，shape[0]:表示行,shape[1]:表示列
    array.reshape 转换数组的形状
"""
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(a)
print(a.shape)  # (9,)当数组是一维时，9表示数组中的元素个数

a1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a1)
print(a1.shape)  # (3, 3)表示3行3列

# 转换成9行1列
a1_1 = a1.reshape(9, 1)
print(a1_1)
# 转换成1行9列
a1_2 = a1.reshape(1, a1.shape[0] * a1.shape[1])
print(a1_2)

a2 = a.reshape(3, 3)
print("a2:", a2)

# 定义一个三维数组
a3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]], [[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("a3:", a3)
print("a3.shape:", a3.shape)  # (4, 2, 3)
# 转换为一维数组

a4 = a3.flatten()
print("a4:", a4)  # [ 1  2  3  4  5  6  7  8  9 10 11 12  1  2  3  4  5  6  7  8  9 10 11 12]
print("a4.shape:", a4.shape)  # (24,)
