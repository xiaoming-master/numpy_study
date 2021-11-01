"""
@author:ming
@file:array_operation.py
@time:2021/10/30
"""
import numpy as np

"""
数组的运算 
 0/0 -> nan
 n/0 -> inf 无穷大
"""

a1 = np.array(range(24)).reshape(2, 3, 4)
print(a1)
a2 = np.array(range(12)).reshape(3, 4)
print(a2)
# 三维与二维运算
a3 = a1 + a2
print("a1 + a2=", a3)
print("-----------------")

a4 = np.array(range(5))
a5 = 2
print("a4=", a4)  # a4= [0 1 2 3 4]
print("a5=", a5)  # a5= 2
print("a4 + a5=", a4 + a5)  # a4 + a5= [2 3 4 5 6]

print("--------------------")
a6 = np.array(range(5))
a7 = np.arange(5, 10)
print("a6=", a6)  # a6= [0 1 2 3 4]
print("a7=", a7)  # a7= [5 6 7 8 9]
print("a6 * a7=", a6 * a7)  # a6 * a7= [ 0  6 14 24 36]

print("-----------------------")
a8 = np.arange(12).reshape(3, 4)
a9 = np.arange(4)
print("a8 / a9 =", a8 / a9)
