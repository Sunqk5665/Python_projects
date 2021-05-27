n = 7  # 楼梯阶数

x = []  # 一个解（长度不固定，1-2数组，表示该步走的台阶数）
X = []  # 一组解


# 冲突检测
def conflict(k):
    global n, x, X

    # 部分解步的步数之和超过总台阶数
    if sum(x[:k + 1]) > n:
        return True

    return False  # 无冲突


# 回溯法（递归版本）
def climb_stairs(k):  # 走第k步
    global n, x, X

    if sum(x) == n:  # 已走的所有步数之和等于楼梯总台阶数
        print(x)
        # X.append(x[:]) # 保存（一个解）
    else:
        for i in [1, 2]:  # 第k步这个元素的状态空间为[1,2]
            x.append(i)
            if not conflict(k):  # 剪枝
                climb_stairs(k + 1)
            x.pop()  # 回溯


# 测试
climb_stairs(0)  # 走第0步