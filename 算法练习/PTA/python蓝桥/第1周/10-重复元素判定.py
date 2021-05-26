n = int(input())
t,f = 0,0
for i in range(n):
    li = input().split()
    se = set(li)
    if len(li)==len(se):
        f += 1    # 不包含重复元素的个数
    else:
        t += 1    # 包含重复元素的个数
print("True=%d, False=%d"%(t,f))