def b(n):
    if n//2==0:
        n = str(n)
        return n
    else:
        x = n%2
        n = n//2
        s = str(x)
        return b(n)+s

print(b(10))