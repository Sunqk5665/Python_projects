import random

x,n = map(int,input().split())
random.seed(x)
f = 0
for i in range(n):
    s = set()  # 集合筛选
    for j in range(23):
        c = random.randint(1,365)  # 产生[1,365]之间的整数
        s.add(c)
    if len(s)<23:
        f += 1


print("rate={:.2f}".format(f/n))