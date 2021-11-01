"""
@author:ming
@file:np_max_min.py
@time:2021/10/31
"""

import numpy as np

"""
最大值和最小值的位置
    np.argmax(arr,axis)
    np.argmin(arr,axis)
        arr ： 表示数组
        axis:表示数轴
numpy 轴（axis）的方向就是朝着某个维度变化的方向
"""

arr = np.arange(24).reshape(2, 3, 4)
print(arr)
max1 = np.argmax(arr, axis=2)
min1 = np.argmin(arr, axis=2)
print("-" * 20)
print(max1)
print(min1)

# 生成一个10行10列对角线值为1的数组
arr1 = np.eye(10, 10)
print(arr1)
