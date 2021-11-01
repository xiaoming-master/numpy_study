"""
@author:ming
@file:np_linalg.py
@time:2021/11/01
"""
import numpy as np

"""
linalg 包
    np.diag(arr,k) 如果arr是二维数组，那么diag()以一维数组的形式返回该数组的对角线
                    如果arr是一维数组，那么diag()返回一个以该数组为对角线的二维数组  
                    k 可以理解为对角线的偏移量，k>0往右偏移，k<0往左偏移
    np.dot(arr,arr) 矩阵的乘法
    np.trace() 计算对角线元素和
    np.det() 计算矩阵的行列式
    np.eig() 计算矩阵的特征值和特征向量
    np.unv() 计算矩阵的逆
    np.qr() qr分解
    np.svd() 计算奇异值分解
    np.solve() 解线性方程组Ax=b, A为矩阵
    np.lstdq() 计算Ax=b的最小二乘解
"""
# arr = np.arange(12).reshape(3, 4)
# diag = np.diag(arr, k=-1)
# print(arr)
# print(diag)

arr1 = np.arange(12).reshape(3, 4)
arr2 = np.arange(4)
print(arr1)
print(arr2)
dot = np.dot(arr1, arr2)
print(dot)
