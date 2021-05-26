def gameHanshu(n):
    s = 1
    lenth = len(str(n))  # lenth->int
    for i in range(1,lenth+1):
        if i!=lenth:
            a = (n//(10**(lenth-i)))%10
        else:
            a = n%10
        s = s * a
    return s

n = int(input())
print(n,end=' ')
while 1:
    n = gameHanshu(n)
    if len(str(n))!=1:
        print(n,end=' ')
    else:
        print(n)
        break
# n=123
# a = (n//(10**(3-1)))%10
# print(a)

# n = int(input())
# print(gameHanshu(54))
# print(type(len(str(n))))
# for i in range(1,4):
#     print(i)

# print(6593//10)