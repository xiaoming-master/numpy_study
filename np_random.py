"""
@author:ming
@file:np_random.py
@time:2021/10/31
"""
import numpy as np

# 创建均匀分布的随机数数组，范围0-1
arr1 = np.random.rand(2, 3, 4)
print(arr1)

# 创建一个标准正态分布的二维数组
arr2 = np.random.randn(3, 4)
print(arr2)

# 创建一个三维数组，值的范围为10-20
arr3 = np.random.randint(10, 20, (2, 3, 4))
print(arr3)

# 创建一个具有均匀分布的三维数组，值的范围0-10
arr4 = np.random.uniform(0, 10, (2, 3, 4))
print(arr4)

# 创建一个指定均值，标准差，维度的正态分布
arr5 = np.random.normal(1.75, 0.1, (2, 3))
print(arr5)

# 深拷贝
arr6 = arr5.copy()
print(arr6)
