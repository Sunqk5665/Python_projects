
n,k = map(int,input().split())
li = [int(i) for i in input().split()]
# print(n,k)
# print(li)
li.sort()
print(li[n-k])

