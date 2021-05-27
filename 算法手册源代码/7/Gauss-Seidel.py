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

U = np.copy(A)  # 求U
DL = np.copy(A)  # 求D-L
for i in range(n):
    for j in range(n):
        if j <= i:
            U[i, j] = 0
        else:
            DL[i, j] = 0
U = 0 - U

# 迭代求解
x = np.ones(n)  # 用于存储迭代过程中x的值
y = np.ones(n)  # 用于存储中间结果
DLU = np.dot(np.linalg.inv(DL), U)  # 对DL求逆，然后和U相乘
DLb = np.dot(np.linalg.inv(DL), b)  # 对DL求逆，然后和b相乘
print('x:', x)
for iteration in range(max):
    # 迭代计算
    y = np.dot(DLU, x) + DLb

    # 判断是否达到精度要求
    if np.max(np.fabs(x - y)) < Delta:
        print('iteration:', iteration)
        break
    # 将y幅值到x，开始下一轮迭代
    x = np.copy(y)
    print('x:', x)