"""
@author:ming
@file:np_update.py
@time:2021/10/31
"""
import numpy as np

"""
更新值 
    nan 为浮点型
"""

arr = np.arange(24).reshape(2, 3, 4)
print(arr)
arr[1, 2, 3] = 0
# print(arr)

arr[1, 1, :] = 0
print(arr)

# 将小于10的值替换为10
arr[arr < 10] = 10
print(arr)

# 获取值>20的元素
a1 = arr[arr > 20]
# print(a1)

# 把值<15的元素替换成5，>15的元素替换成15
a2 = np.where(arr < 15, 5, 15)
print(a2)

arr = np.arange(24).reshape(2, 3, 4)

# 小于8的替换成8，大于18的替换成18
# a3 = np.clip(arr, 8, 18)
# print(a3)
a4 = arr.clip(8, 18)
print(a4)

# 将某个值替换为nan
arr = arr.astype(float)
arr[1, 1, :] = np.nan
print(arr)
