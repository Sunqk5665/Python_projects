n,m = map(int,input().split())
li1 = []
li2 = []
for i in range(n):
    f,name = input().split()
    li1.append([f,name])

for j in range(m):
    a,s = map(int,input().split())
    li2.append([a,s])
index = 0  # 记录当前lit1[]下标
for i in range(m):
    if li2[i][0]==0 and li1[index][0]=='0':
        index = ((n + index) - li2[i][1]) % n
        res = li1[index][1]
    if li2[i][0]==1 and li1[index][0]=='0':
        index = (index + li2[i][1]) % n
        res = li1[index][1]
    if li2[i][0]==0 and li1[index][0]=='1':
        index = (index + li2[i][1]) % n
        res = li1[index][1]
    if li2[i][0]==1 and li1[index][0]=='1':
        index = ((n + index) - li2[i][1]) % n
        res = li1[index][1]

print(li1[index][1])
# li = [[1,2],[3,4],[5,6]]
# for i in range(3):
#     print(li[i][0])