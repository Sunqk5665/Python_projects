'''
图的遍历

从一个节点出发，不重复地经过所有其它节点后，回到出发节点。找出所有的路径
'''

# 用邻接表表示图
n = 6  # 节点数
a, b, c, d, e, f = range(n)  # 节点名称
graph = [
    {b, c},
    {c, d, e},
    {a, d},
    {c},
    {f},
    {c, d}
]

x = [0] * (n + 1)  # 一个解（n+1元数组，长度固定）
X = []  # 一组解


# 冲突检测
def conflict(k):
    global n, graph, x

    # 第k个节点，是否前面已经走过
    if k < n and x[k] in x[:k]:
        return True

    # 回到出发节点
    if k == n and x[k] != x[0]:
        return True

    return False  # 无冲突


# 图的遍历
def dfs(k):  # 到达（解x的）第k个节点
    global n, a, b, c, d, e, f, graph, x, X

    if k > n:  # 解的长度超出，已走遍n+1个节点 （若不回到出发节点，则 k==n）
        print(x)
        # X.append(x[:])
    else:
        for node in graph[x[k - 1]]:  # 遍历节点x[k]的邻接节点（x[k]的所有状态）
            x[k] = node
            if not conflict(k):  # 剪枝
                dfs(k + 1)


# 测试
x[0] = e  # 出发节点
dfs(1)  # 开始处理解x中的第2个节点