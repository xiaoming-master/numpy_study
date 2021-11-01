"""
@author:ming
@file:array_create.py
@time:2021/10/29
"""
import random

import numpy as np

"""
使用numpy创建数组
    1、np.array([]/range(),dtype="int32")
    2、np.arange(start,end,step)
    
    a.dtype 表示数组元素的数据类型
    a.astype="" 转换数组的数据类型
    random.random() 生成0-1之间的小数
    round(num,n) 保留n位小数
    np.round(array,n) 为数组中的小数保留n位小数
"""
"""
数据类型：
        类型          类型代码        说明
    int8、uint8       i1、u1        有符号和无符号的8位（1字节）整型
    int16、uint16     i2、u2        有符号和无符号的16位（2字节）整型
    int32、uint32     i4、u4        有符号和无符号的32位（4字节）整型
    int64、uint64     i8、u8        有符号和无符号的64位（8字节）整型
    float16           f2           半精度浮点数
    float32           f4/f         标准单精度浮点数，与C的float兼容
    float64           f8/d         标准的双精度浮点数，与C的double和python的float兼容
    float128          f16/g        扩展精度浮点数
    bool                ?          存储True和False值的布尔类型
    complex64、complex128、complex256 c8、c16、c32分别用两个32位、64位或128位表示的复数
"""

# 创建数组,dtype 指定元素数据类型
a1 = np.array([1, 2, 3, 4, 5], dtype="int32")
print(a1)
print(type(a1))
# 输出数组的数据类型
print(a1.dtype)

# 创建一个数组，数据为2-9,步长为2
a2 = np.arange(2, 10, 2)
print(a2)
print(a2.dtype)

# 创建一个值为bool类型的数组
a3 = np.array([1, 0, 1, 1, 0, 0], dtype=bool)
print(a3)
print(a3.dtype)  # bool

# 将a3的数据类型从bool转换为int8
a4 = a3.astype("int8")
print(a4.dtype)  # int8

# 生成10个 0-1 的小数 保留3为小数
data = [round(random.random(), 3) for i in range(10)]
# 创建数组
a5 = np.array(data)
print(a5)
print(a5.dtype)

# 保留两位小数
a6 = np.round(a5, 2)
print(a6)
