import numpy as np

max = 100  # 迭代次数上限
Delta = 0.01
m = 2  # 阶数：矩阵为2阶
n = 3  # 维数：3X3的矩阵

shape = np.full(m, n)
shape = tuple(shape)


def read_tensor(f, shape):  # 读取张量
    data = []
    for i in range(n ** (m - 1)):
        line = f.readline()
        data.append(list(map(eval, line.split(","))))
    return np.array(data).reshape(shape)


def read_vector(f):  # 读取向量
    line = f.readline()
    line = line.replace("\n", "")
    line = list(map(eval, line.split(",")))
    return np.array(line)


# 读取数据
f = open("123.txt")
A = read_tensor(f, shape)  # 读取矩阵A
b = read_vector(f)  # 读取b
f.close()
print('A:')
print(A)
print('b:', b)

# 求LU=L+U
LU = np.copy(A)
for i in range(n):
    LU[i, i] = 0
LU = 0 - LU

# 求D:系数矩阵的对角线元素
D = np.copy(A)
D = D + LU

# 迭代求解
x = np.ones(n)  # 用于存储迭代过程中x的值
y = np.ones(n)  # 用于存储中间结果
DLU = np.dot(np.linalg.inv(D), LU)  # 对D求逆，然后和LU相乘
Db = np.dot(np.linalg.inv(D), b)
print('x:', x)
for iteration in range(max):
    # 迭代计算
    y = np.dot(DLU, x) + Db

    # 判断是否达到精度要求
    if np.max(np.fabs(x - y)) < Delta:
        print('iteration:', iteration)
        break
    # 将y幅值到x，开始下一轮迭代
    x = np.copy(y)
    print('x:', x)