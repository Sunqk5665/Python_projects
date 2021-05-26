num = int(input())
prime = 2
st = ''
while(num>1):
    if (num % prime==0):
        num /= prime
        st += str(prime)
    else:
        prime += 1

print(int(st)%(10**9+7))
