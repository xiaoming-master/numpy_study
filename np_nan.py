"""
@author:ming
@file:np_nan.py
@time:2021/10/31
"""
import numpy as np

"""
关于nan 
    arr.sum(axis) np.sum(arr,axis)不指定轴就计算整个数组的和，否者就计算指定数轴上的和
    arr.mean(axis) np.mean(arr,axis) 不指定轴就计算整个数组的平均数，否者就计算指定数轴上的平均数
    np.median(arr,axis=1) 不指定轴就计算整个数组的中位数，否者就计算指定数轴上的中位数
    np.max(arr,axis) arr.max(axis)
    np.min(arr,axis) arr.min(axis)
    np.ptp(arr,axis) arr.ptp(axis) 计算极值 max-min
    np.std(arr,axis) arr.std(axis) 计算标准差
    np.var(arr,axis) arr.var(axis) 计算方差
    arr.cumsum(axis) 产生一个数组，元素的值是当前元素沿着轴方向前面的所有元素（包括当前元素在内）的累加和
    arr.cumprod(axis) 产生一个数组，元素的值是当前元素沿着轴方向前面的所有元素（包括当前元素在内）的累积
"""
# 随机种子
np.random.seed(10)
arr = np.random.randint(0, 30, (3, 4)).astype(float)
arr[2, 2] = np.nan
print(arr)

# 统计非0的元素个数
print(np.count_nonzero(arr))

# 统计不是nan的元素个数
print(np.count_nonzero(arr != arr))

# 判断元素是否为nan,返回一个数组
print(np.isnan(arr))

# 将非nan的元素替换为1
# arr[np.isnan(arr)] = 1
# print(arr)


# s = arr.sum(axis=0)
# print(s)
#
# mean = arr.mean(axis=1)
# print(mean)
#
# median = np.median(arr, axis=1)
# print(median)
# print(np.max(arr, axis=0))

# ptp = np.ptp(arr, axis=1)
# ptp = arr.ptp(axis=1)
# print(ptp)

# std = arr.std(axis=0)
# std = np.std(arr, axis=0)
# print(std)

# var = np.var(arr, axis=0)
var = arr.var(axis=0)
print(var)
