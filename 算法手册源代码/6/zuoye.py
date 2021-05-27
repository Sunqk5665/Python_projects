'''
最佳作业调度问题

tji          机器1     机器2
作业1         2          1
作业2         3          1
作业3         2          3

'''

n = 3  # 作业数
# n个作业分别在两台机器需要的时间
t = [[2, 1],
     [3, 1],
     [2, 3]]

x = [0] * n  # 一个解（n元数组，xi∈J）
X = []  # 一组解

best_x = []  # 最佳解（一个调度）
best_t = 0  # 机器2最小时间和


# 冲突检测
def conflict(k):
    global n, x, X, t, best_t

    # 部分解内的作业编号x[k]不能超过1
    if x[:k + 1].count(x[k]) > 1:
        return True

    # 部分解的机器2执行各作业完成时间之和未有超过 best_t
    # total_t = sum([sum([y[0] for y in t][:i+1]) + t[i][1] for i in range(k+1)])
    j2_t = []
    s = 0
    for i in range(k + 1):
        s += t[x[i]][0]
        j2_t.append(s + t[x[i]][1])
    total_t = sum(j2_t)
    if total_t > best_t > 0:
        return True

    return False  # 无冲突


# 最佳作业调度问题
def dispatch(k):  # 到达第k个元素
    global n, x, X, t, best_t, best_x

    if k == n:  # 超出最尾的元素
        # print(x)
        # X.append(x[:]) # 保存（一个解）

        # 根据解x计算机器2执行各作业完成时间之和
        j2_t = []
        s = 0
        for i in range(n):
            s += t[x[i]][0]
            j2_t.append(s + t[x[i]][1])
        total_t = sum(j2_t)
        if best_t == 0 or total_t < best_t:
            best_t = total_t
            best_x = x[:]
    else:
        for i in range(n):  # 遍历第k个元素的状态空间，机器编号0~n-1，其它的事情交给剪枝函数
            x[k] = i
            if not conflict(k):  # 剪枝
                dispatch(k + 1)


# 测试
dispatch(0)
print(best_x)  # [0, 2, 1]
print(best_t)  # 18