data = [[0, 2, 8, 1, 0, 0, 0, 0],
        [2, 0, 6, 0, 1, 0, 0, 0],
        [8, 6, 0, 7, 5, 1, 2, 0],
        [1, 0, 7, 0, 0, 0, 9, 0],
        [0, 1, 5, 0, 0, 3, 0, 8],
        [0, 0, 1, 0, 3, 0, 4, 6],
        [0, 0, 2, 9, 0, 4, 0, 3],
        [0, 0, 0, 0, 8, 6, 3, 0]]


# 转换数据格式
def build_graph(data):
    G = {}
    for i in range(len(data)):
        G[str(i)] = {}
        for j in range(len(data[i])):
            if data[i][j] != 0:
                G[str(i)][str(j)] = data[i][j]
    return G


G = build_graph(data)


# 返回U中包含定点v的连通分支的名字。这个运算用来确定某条边的两个端点所属的连通分支
def find(C, u):
    if C[u] != u:
        C[u] = find(C, C[u])
    return C[u]


# 将C，R两个连通分支连接起来
def union(C, R, u, v):
    u, v = find(C, u), find(C, v)
    if R[u] > R[v]:
        C[v] = u
    else:
        C[u] = v
    if R[u] == R[v]:
        R[v] += 1


def kruskal(G):
    E = [(G[u][v], u, v) for u in G for v in G[u]]
    print(E)
    T = set()
    C, R = {u: u for u in G}, {u: 0 for u in G}
    print(C, R)
    for _, u, v in sorted(E):
        print(_, u, v)
        if find(C, u) != find(C, v):
            T.add((u, v))
            union(C, R, u, v)
    return T


print(list(kruskal(G)))