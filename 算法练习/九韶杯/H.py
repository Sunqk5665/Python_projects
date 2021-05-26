n,m = map(int,input().split())
li = []
for i in range(m):
    a,b = map(int,input().split())
    li.append([a,b])

if li[m-1][1]==n:
    print(m)
else:
    print(-1)

# print(n,m)