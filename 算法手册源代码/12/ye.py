n = 3  # n个传教士、n个野人
m = 2  # 船能载m人

x = []  # 一个解，就是船的一系列状态
X = []  # 一组解

is_found = False  # 全局终止标志


# 计算船的合法状态空间（二维）
def get_states(k):  # 船准备跑第k趟
    global n, m, x

    if k % 2 == 0:  # 从左到右，只考虑原左岸人数
        s1, s2 = n - sum(s[0] for s in x), n - sum(s[1] for s in x)
    else:  # 从右到左，只考虑原右岸人数（将船的历史状态累加可得！！！）
        s1, s2 = sum(s[0] for s in x), sum(s[1] for s in x)

    for i in range(s1 + 1):
        for j in range(s2 + 1):
            if 0 < i + j <= m and (i * j == 0 or i >= j):
                yield [(-i, -j), (i, j)][k % 2 == 0]  # 生成船的合法状态


# 冲突检测
def conflict(k):  # 船开始跑第k趟
    global n, m, x

    # 若船上载的人与上一趟一样（会陷入死循环！！！！）
    if k > 0 and x[-1][0] == -x[-2][0] and x[-1][1] == -x[-2][1]:
        return True

    # 任何时候，船上传教士人数少于野人，或者无人，或者超载（计算船的合法状态空间时已经考虑到了。）
    # if 0 < abs(x[-1][0]) < abs(x[-1][1]) or x[-1] == (0, 0) or abs(sum(x[-1])) > m:
    #    return True

    # 任何时候，左岸传教士人数少于野人
    if 0 < n - sum(s[0] for s in x) < n - sum(s[1] for s in x):
        return True

    # 任何时候，右岸传教士人数少于野人
    if 0 < sum(s[0] for s in x) < sum(s[1] for s in x):
        return True

    return False  # 无冲突


# 回溯法
def backtrack(k):  # 船准备跑第k趟
    global n, m, x, is_found

    if is_found: return  # 终止所有递归

    if n - sum(s[0] for s in x) == 0 and n - sum(s[1] for s in x) == 0:  # 左岸人数全为0
        print(x)
        is_found = True
    else:
        for state in get_states(k):  # 遍历船的合法状态空间
            x.append(state)
            if not conflict(k):
                backtrack(k + 1)  # 深度优先
            x.pop()  # 回溯


# 测试
backtrack(0)