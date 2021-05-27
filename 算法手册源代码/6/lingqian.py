n = 4
a = [10, 5, 2, 1]  # 四种面额
b = [3, 5, 7, 12]  # 对应的硬币数目（状态空间）

m = 53  # 给定的金额

x = [0] * n  # 一个解（n元0-b[k]数组）
X = []  # 一组解

best_x = []  # 最佳解
best_num = 0  # 最少硬币数目


# 冲突检测
def conflict(k):
    global n, m, x, X, a, b, best_num

    # 部分解的金额已超
    if sum([p * q for p, q in zip(a[:k + 1], x[:k + 1])]) > m:
        return True

    # 部分解的金额加上剩下的所有金额不够
    if sum([p * q for p, q in zip(a[:k + 1], x[:k + 1])]) + sum([p * q for p, q in zip(a[k + 1:], b[k + 1:])]) < m:
        return True

    # 部分解的硬币个数超best_num
    num = sum(x[:k + 1])
    if 0 < best_num < num:
        return True

    return False  # 无冲突


# 回溯法（递归版本）
def subsets(k):  # 到达第k个元素
    global n, a, b, x, X, best_x, best_num

    if k == n:  # 超出最尾的元素
        # print(x)
        X.append(x[:])  # 保存（一个解）

        # 计算硬币数目，若最佳，则保存
        num = sum(x)
        if best_num == 0 or best_num > num:
            best_num = num
            best_x = x[:]
    else:
        for i in range(b[k] + 1):  # 遍历元素 a[k] 的可供选择状态: 0, 1, 2, ..., b[k] 个硬币
            x[k] = i
            if not conflict(k):  # 剪枝
                subsets(k + 1)


# 测试
subsets(0)
print(best_x)