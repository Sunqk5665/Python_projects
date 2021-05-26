# def jiecheng(n):
#     if n<=1:
#         return 1
#     else:
#         return n*jiecheng(n-1)
# n = int(input())
# print(jiecheng(n))

n = int(input())
for i in range(n-1,0,-1):
    n *= i
print(n)