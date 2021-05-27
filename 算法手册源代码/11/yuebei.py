m=int(input("请输入一个正整数："))
n=int(input("请输入第二个正整数："))
a=m
b=n
if a>b:
    t=a
    a=b
    t=b
while a!=0:
    r=b%a
    b=a
    a=r
max=b
min=m*n//max
print("{}和{}的最大公约数是{}，最小公倍数是{}".format(m,n,max,min))