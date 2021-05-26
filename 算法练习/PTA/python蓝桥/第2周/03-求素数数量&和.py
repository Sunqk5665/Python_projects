# 若是这个题使用枚举法则是时间复杂度就显得比较大了，所以这里可以去考虑另外一种时间复杂度较小的算法
# 这里我们要认清一个事实：如果 x 是一个质数，那么大于 x 的 x 的倍数2x,3x,....一定不是质数，
# 因此我们可以从这里入手，从小到大遍历每个数，如果这个数为质数，
# 则将其所有的倍数都标记为合数(除了该质数本身)。这就是埃氏筛思想。

n = int(input())

li = [1 for i in range(n)]  # li = [1, 1, 1, 1, 1, 1，... ,1] #设置标志
Count = 0
Sum = 0
for i in range(2,n):
    if li[i]:
        Count += 1  # 素数个数
        Sum += i  # 求和
        print(i,end=' ')
        if i*i<n:
            for j in range(i*i,n,i):
                li[j] = 0
print("\namount={}, sum={}".format(Count, Sum))

# li = [1 for i in range(6)]
# print(li)
# def sushu(shu):
#     if shu == 1:
#         return False
#     for i in range(2,shu//2+1):
#         if shu%i==0:
#             return False
#     else:
#         return True
#
# num = int(input())
# s,count = 0,0
#
# for i in range(1,num):
#     if sushu(i):
#         s += i
#         count += 1
# print("amount={}, sum={}".format(count,s))

# n = int(input())
# li = [1 for i in range(n)]
# Count = 0
# Sum = 0
# for i in range(2,n):
#     if li[i]==1:
#         Count += 1
#         Sum += i
#         if i*i<n:
#             for j in range(i*i,n,i):
#                 li[j]=0
# print("amount={}, sum={}".format(Count,Sum))