def euler(n):
    ans = n
    for i in range(2,9999999999):
        if i*i>n:
            break
        if(n % i ==0):
            ans -= ans/i
            while(n % i ==0):
                n /= i
    if(n > 1):
        ans -= ans/n
    return ans

if __name__=='__main__':
    n = int(input())
    print(int(euler(n)))
# import math
# print(math.gcd(8,1))