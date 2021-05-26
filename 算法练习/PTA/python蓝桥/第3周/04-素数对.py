def prime(num):
    if num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        for i in range(2,int(n**0.5)+1):
            if num % i == 0:
                return False
        return True

n = int(input())
res = 0
if n < 2:
    res = 0
else:
    for i in range(2,n+1):
        if prime(i) and prime(n+1-i):
            res += 1
print(res)