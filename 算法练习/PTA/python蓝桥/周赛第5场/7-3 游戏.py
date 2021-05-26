n,m = map(int,input().split())
# print(n,m)
lst = {}
for i in range(1,n+1):
    lst[i] = i
while (n!=1):
    for key in lst.keys():
        if key % m == 0:
            del(lst[key])
    i = 0
    for key in lst.keys():
        key = i + 1

    n = len(lst)
print(lst)