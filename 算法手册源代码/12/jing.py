'''
2a + b = deep
3b + c = deep
4c + d = deep
5d + e = deep
6e + a = deep
---->
a = b + c/2
b = c + d/3
c = d + e/4
d = e + a/5
---->
c % 2 = 0
d % 3 = 0
e % 4 = 0
a % 5 = 0

'''

def fun():
    e = 0
    while True:
        e += 4
        a = 0
        while True:
            a += 5
            d = e + a / 5
            c = d + e / 4
            if c % 2 != 0 or d % 3 != 0:
                continue
            b = c + d / 3
            if b + c / 2 < a:
                break
            if b + c / 2 == a:
                deep = 2 * a + b
                print('a--> %d, b--> %d, c--> %d, d--> %d, e--> %d, deep--> %d' % (a, b, c, d, e, deep))
                return a, b, c, d, e, deep


print(fun())
