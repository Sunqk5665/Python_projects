res = []
n = int(input())
res.append(1)
res.append(2)
for i in range(2,n):
    res.append(res[i-1] + res[i-2])
print(res[n-1])
