import numpy as np

"""创建不同形式的矩阵"""
# 创建矩阵
array = np.array([[1, 2, 3],
                  [2, 3, 4]])
# 创建全部为0,1的矩阵
a = np.zeros((3, 4))
b = np.ones((3, 4))
# 创建有序矩阵：从10到19，步长1
c = np.arange(10, 20, 1)
# 创建有序矩阵：0到11，3行4列
d = np.arange(12).reshape((3, 4))
# 创建有序矩阵线段：1到5之间5个数值
e = np.linspace(1, 5, 6).reshape((2, 3))
# 随机生成0~1之间2行4列的矩阵
f = np.random.random((2, 4))

"""属性"""
# 有几维
print("number of dim:", array.ndim)
# 有几行几列
print("shape:", array.shape)
# 大小：行*列
print("size:", array.size)

"""矩阵之间的运算"""
a1 = np.array([1, 1],
              [0, 1])
b1 = np.arange(4).reshape((2, 2))
# 减法
c1 = a1 - b1
# 加法
c2 = a1 + b1
# 乘方
c3 = a1**2
# 逐个相乘
c4 = a*b
# 矩阵乘法
c_dot = np.dot(a, b)
# 矩阵的求和，最大值，最小值:axis=1列中求值axis=0行中求值
np.sum(a, axis=1)
np.min(a)
np.max(a)

A = np.arange(3, 15).reshape((3, 4))
# 矩阵里面的最小值、最大值、平均值、中位数、累加
print(np.argmin(A))
print(np.argmax(A))
print(np.average(A))
print(np.median(A))
print(np.cumsum(A))
print(np.diff(A))

# 矩阵逐行排序、反向
print(np.sort(A))
print(np.transpose(A))
print(A.T)
# 索引输出第2行第3列的数值
print(A[2, 3])
# 索引输出第1行所有的数值
print(A[1, :])
# 索引输出第2列所有的数值
print(A[:, 3])

"""迭代"""
A = np.arange(3, 15).reshape((3, 4))
for row in A:
    # 输出每一行
    print(row)

for column in A.T:
    # 输出每一列
    print(column)

for item in A.flat:
    # 输出每一个值：flat把矩阵转换成一行
    print(item)

"""array合并"""
A = np.array([1, 1, 1])
B = np.array([2, 2, 2])
# 上下合并
print(np.vstack((A, B)))
# 左右合并
print(np.hstack((A, B)))
# A矩阵的行、纵向加个维度
print(A[np.newaxis, :])
print(A[:, np.newaxis])
# 横向变纵向
A = np.array([1, 1, 1])[:, np.newaxis]
B = np.array([2, 2, 2])[:, np.newaxis]
# 合并
C = np.concatenate((A, B, B, A), axis=1)

"""array分割"""
A = np.arange(12).reshape((3, 4))
# 对列进行分割成2个array
print(np.split(A, 2, axis=1))
# 对列进行不等分割3个array
print(np.array_split(A, 3, axis=1))
# 纵向分割
print(np.vsplit(A, 3))
# 横向分割
print(np.hsplit(A, 2))














