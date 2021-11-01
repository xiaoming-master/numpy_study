"""
@author:ming
@file:np_loadtxt.py
@time:2021/10/31
"""
import random

import numpy as np
import csv

"""
从csv文件中加载数据 
    np.loadtxt(fname, dtype=float, comments='#', delimiter=None,
            converters=None, skiprows=0, usecols=None, unpack=False,
            ndmin=0, encoding='bytes', max_rows=None, *, like=None)
            fname: 文件，字符串，产生器， .gz或bz2压缩文件
            dtype: 数据类型
            delimiter: 分隔符
            skiprows: 跳过多少行
            usecols: 读取指定列
            unpack: 类似于转置
"""

# 生成1w条数据
# file = open("movie_data.csv", mode="a", encoding="utf-8")
# writer = csv.writer(file)
# part_data = []
# for i in range(20):
#     for j in range(500):
#         # 生成一个随机数,播放量
#         play_times = random.randint(1000, 500000)
#         # 喜欢
#         likes = random.randint(0, play_times)
#         # 不喜欢
#         dislikes = random.randint(0, play_times - likes)
#         # 评论
#         comments = random.randint(0, 500000)
#         data = [play_times, likes, dislikes, comments]
#         part_data.append(data)
#     writer.writerows(part_data)
#     part_data.clear()
# file.close()

#
# # 矩阵转置的三种方法
# a = np.arange(12).reshape(3, 4)
# print(a)
#
# print(a.transpose())
#
# print(a.T)
# print(a.swapaxes(1, 0))

data = np.loadtxt("movie_data.csv", dtype=int, delimiter=",")
print(data)
print("-" * 20)
# 获取第1行
# print(data[0])
print("-" * 20)
# 对行切片操作，取第2行后面的所有行
# print(data[1:])
# 取第2行到第4行
# print(data[1:5])

# 取多个不连续行
# print(data[[2, 4, 6]])

print("-" * 20)
print("取列")
# 取第1行第1列的数据
# print(data[0, 0])

# 取第2行所有的列，表示取第1行
# print(data[1, :])

# 取第3行后买那个所有的列
# print(data[2:, :])

# 取指定的不连续的行
# print(data[[1, 3, 5], :])

# 取第1列
# print(data[:, 0])

# 取第3列后面的所有列
# print(data[:, 2:])

# 取第2列和第3列
# print(data[:, 1:3])

# 取指定的列
# print(data[:, [0, 2, 3]])

# 取多行多列 第1行到第3行（不包括第3行），第1列到第3列（不包括第三列）
# print(data[1:3, 1:3])

# 取指定行，第2列后的所有值
# print(data[[0, 1, 2], 1:])

# 取多个点的值 (1,0),(3,2),(5,3)
# print(data[[1, 3, 5], [0, 2, 3]])
