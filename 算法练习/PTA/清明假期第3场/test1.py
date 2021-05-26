# s = 1
# for i in range(10,0,-1):
#     s = s*i
# print(s)
def jiecheng(n):
    s = 1
    for i in range(n,0,-1):
        s = s*i
    return s
def C(n,m):
    a=b=1
    for i in range(m,m-n,-1):
        a = a*i
    for j in range(n,0,-1):
        b = b*j
    return a/b
n = 100
res = (jiecheng(n)*(C(n,2*n)-C(n+1,2*n)))
print(res%1000000007)