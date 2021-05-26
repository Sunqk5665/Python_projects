def gcd_test_two(a,b):
    if a>b:
        a,b=b,a
    if b%a==0:
        return a
    else:
        return gcd_test_two(a,b%a)

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(gcd_test_two(a,b))