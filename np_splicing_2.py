"""
@author:ming
@file:np_splicing_2.py
@time:2021/10/31
"""

import csv
import random
import numpy as np

# 生成1w条数据
# file = open("uk_movie_data.csv", mode="a", encoding="utf-8")
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

# 读取文件
us_data = np.loadtxt("us_movie_data.csv", delimiter=",", dtype=int)
uk_data = np.loadtxt("uk_movie_data.csv", delimiter=",", dtype=int)

# 为数据添加国家区分标识符 0-us,1-uk
# 生成一个与 us_data 相同行数的一列全为0的数组
us_mark = np.zeros((us_data.shape[0], 1), dtype=int)
# 生成一个与 uk_data 相同行数的一列全为1的数组
uk_mark = np.ones((uk_data.shape[0], 1), dtype=int)

# 为us_data水平拼接数据
us_data = np.hstack((us_data, us_mark))

# 为uk_data水平拼接数据
uk_data = np.hstack((uk_data, uk_mark))

# 垂直平解us uk的数据
data = np.vstack((us_data, uk_data))
print(data)
