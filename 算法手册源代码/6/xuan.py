'''
选排问题

从n个元素中挑选m个元素进行排列，每个元素最多可重复r次。其中m∈[2,n]，r∈[1,m]。

'''

n = 4
a = ['a', 'b', 'c', 'd']

m = 3  # 从4个中挑3个
r = 2  # 每个元素最多可重复2

x = [0] * m  # 一个解（m元0-1数组）
X = []  # 一组解


# 冲突检测
def conflict(k):
    global n, r, x, X, a

    # 部分解内的元素x[k]不能超过r
    if x[:k + 1].count(x[k]) > r:
        return True

    return False  # 无冲突


# 用子集树模板实现选排问题
def perm(k):  # 到达第k个元素
    global n, m, a, x, X

    if k == m:  # 超出最尾的元素
        print(x)
        # X.append(x[:]) # 保存（一个解）
    else:
        for i in a:  # 遍历x[k-1]的状态空间a，其它的事情交给剪枝函数！
            x[k] = i
            if not conflict(k):  # 剪枝
                perm(k + 1)


# 测试
perm(0)  # 从x[0]开始排列