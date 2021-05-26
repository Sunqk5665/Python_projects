n = int(input())
lst = []
for i in range(n):
    a = [int(i) for i in input().split()]
    lst.append(a)
for i in lst:
    for j in i:
        for k in lst:
            pass


# a = [[1,2],[3,4]]
# b = 1
# print(b in a)