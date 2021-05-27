'''求集合{1, 2, 3, 4}的所有子集'''

n = 4
# a = ['a','b','c','d']
a = [1, 2, 3, 4]
x = []  # 一个解（n元0-1数组）
X = []  # 一组解


# 冲突检测：无
def conflict(k):
    global n, x, X, a

    return False  # 无冲突


# 一个例子
# 冲突检测：奇偶性相同，且和小于8的子集
def conflict2(k):
    global n, x, X, a

    if k == 0:
        return False

    # 根据部分解，构造部分集
    s = [y[0] for y in filter(lambda s: s[1] != 0, zip(a[:k + 1], x[:k + 1]))]
    if len(s) == 0:
        return False
    if 0 < sum(map(lambda y: y % 2, s)) < len(s) or sum(s) >= 8:  # 只比较 x[k] 与 x[k-1] 奇偶是否相间
        return True

    return False  # 无冲突


# 子集树递归模板
def subsets(k):  # 到达第k个元素
    global n, x, X

    if k >= n:  # 超出最尾的元素
        # print(x)
        X.append(x[:])  # 保存（一个解）
    else:
        for i in [1, 0]:  # 遍历元素 a[k] 的两种选择状态:1-选择，0-不选
            x.append(i)
            if not conflict2(k):  # 剪枝
                subsets(k + 1)
            x.pop()  # 回溯


# 根据一个解x，构造一个子集
def get_a_subset(x):
    global a

    return [y[0] for y in filter(lambda s: s[1] != 0, zip(a, x))]


# 根据一组解X, 构造一组子集
def get_all_subset(X):
    return [get_a_subset(x) for x in X]


# 测试
subsets(0)

# 查看第3个解，及对应的子集
# print(X[2])
# print(get_a_subset(X[2]))

print(get_all_subset(X))