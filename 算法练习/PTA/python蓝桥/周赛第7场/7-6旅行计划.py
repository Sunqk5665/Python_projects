import math

n,m,t = input().split()
maxn = int(math.pow(10,3))
INF = float('fin')
maps=[maxn][maxn]
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            maps[i][j]==0
        else:
            maps[i][j]==INF
while(m-1):
    u,v,w = print().split()
    maps[u][v] = w