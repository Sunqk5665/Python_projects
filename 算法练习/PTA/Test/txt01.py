
#素数
n = int(input())
li = [1 for i in range(n)]
amo = 0
count = 0
for i in range(2,n):
    if li[i]:
        amo += 1
        count += i
        if i*i<n:
            for j in range(i*i,n,i):
                li[j] = 0
print("amount={}, sum={}".format(amo,count))


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
#
# print("amount={}, sum={}".format(count,s))