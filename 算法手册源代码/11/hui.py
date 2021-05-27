import math
def isPrimeNumber(num):
    i = 2
    x = math.sqrt(num)
    while i < x:
        if num % i == 0:
            return False
        i += 1
    return True

def Reverse(num):
    rNum = 0
    while num:
        rNum = rNum * 10 + num % 10
        num //= 10
    return rNum


def RPrimeNumber(num):
    arr = []
    i = 2
    while i < num:
        if isPrimeNumber(i) and i == Reverse(i):
            arr.append(i)
        i += 1
    return arr

print(RPrimeNumber(1000))
