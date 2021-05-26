def weight(x):
    if x % 2 == 0:
        x = x/2
    else:
        x = 3 * x + 1
    return x

l,r = map(int,input().split())
# k = int(input())
s = []
for i in range(l,r+1):
    s.append(weight(i))
print(s)




# print(s)