# prim算法
from heapq import heappush, heappop
import math

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


# print(G)

def prim(G, source):
    P = {}  # parent字典
    Q = [(0, None, source)]  # 优先队列

    while Q:
        _, p, u = heappop(Q)  # 将权值最小的元素弹出
        if u in P:  # 如果节点u在P里面的话
            continue
        P[u] = p  # 节点u链接节点p
        for v, w in G[u].items():  # 将所有现有邻接线的权重添加入优先队列中
            heappush(Q, (w, u, v))  # 权重, 先节点, 节点
    return P


subtree = prim(G, "0")

print(subtree)