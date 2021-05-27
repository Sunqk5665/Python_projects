n = 4
a = ['a', 'b', 'c', 'd']

x = [0] * n  # 一个解（n元0-1数组）
X = []  # 一组解


# 冲突检测：无
def conflict(k):
    global n, x, X, a

    return False  # 无冲突


# 用子集树模板实现全排列
def perm(k):  # 到达第k个元素
    global n, a, x, X

    if k >= n:  # 超出最尾的元素
        print(x)
        # X.append(x[:]) # 保存（一个解）
    else:
        for i in set(a) - set(x[:k]):  # 遍历，剩下的未排的所有元素看作元素x[k-1]的状态空间
            x[k] = i
            if not conflict(k):  # 剪枝
                perm(k + 1)


# 测试
perm(0)  # 从x[0]开始
