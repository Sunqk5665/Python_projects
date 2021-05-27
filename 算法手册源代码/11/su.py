def isPrimeNumber(n, s):
    for k in s:
        if k * k > n: break
        if n % k == 0: return None
    return n

prime = []
for n in range(2, 100):
    res = isPrimeNumber(n, prime)
    if res: prime.append(res)

print(prime)
