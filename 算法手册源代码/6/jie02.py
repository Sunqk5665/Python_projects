'''求[1,2,3,4]的全排列'''

n = 4
x = [1, 2, 3, 4]  # 一个解
X = []  # 一组解


# 冲突检测：无
def conflict(k):
    global n, x, X

    return False  # 无冲突


# 一个例子
# 冲突检测：元素奇偶相间的排列
def conflict2(k):
    global n, x, X

    if k == 0:  # 第一个元素，肯定无冲突
        return False

    if x[k - 1] % 2 == x[k] % 2:  # 只比较 x[k] 与 x[k-1] 奇偶是否相同
        return True

    return False  # 无冲突


# 排列树递归模板
def backkrak(k):  # 到达第k个位置
    global n, x, X

    if k >= n:  # 超出最尾的位置
        print(x)
        # X.append(x[:]) # 注意x[:]
    else:
        for i in range(k, n):  # 遍历后面第 k~n-1 的位置
            x[k], x[i] = x[i], x[k]
            if not conflict2(k):  # 剪枝
                backkrak(k + 1)
            x[i], x[k] = x[k], x[i]  # 回溯


# 测试
backkrak(0)