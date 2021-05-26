n,k = map(int, input().split())
s = 1
i = 0
while(k):
    s *= (n**(int(k & 1)*(2**i)))
    k >>= 1
    i += 1
print(s%(10**9+7))