l=0
m=0
n=0
o=0
p=0
q=0
r=0
s=0
t=0
u=0
gongzi = []
for k in range(0, 5):
    gongzi.append(float(input('请输入第{}个人的工资数：'.format(k+1))))
print('***************************************')
for k in range(0, 5):
    if gongzi[k] >= 100:
        a = gongzi[k] // 100
        gongzi[k] = gongzi[k] - 100 * a
        print('{}张一百的'.format(int(a)))
        l = int(l + a)
    if gongzi[k] >= 50:
        b = gongzi[k] // 50
        gongzi[k] = gongzi[k] - 50 * b
        print('{}张五十的'.format(int(b)))
        m =int(m + b)
    if gongzi[k] >= 20:
        c = gongzi[k] // 20
        gongzi[k] = gongzi[k] - 20 * c
        print('{}张二十的'.format(int(c)))
        n = int(n + c)
    if gongzi[k] >= 10:
        d = gongzi[k] // 10
        gongzi[k] = gongzi[k] - 10 * d
        print('{}张十块的'.format(int(d)))
        o = int(o + d)
    if gongzi[k]  >= 5:
        e = gongzi[k] // 5
        gongzi[k] = gongzi[k] - 5 * e
        print('{}张五元的'.format(int(e)))
        p =int( p + e)
    if gongzi[k]  >= 1:
        f = gongzi[k] // 1
        gongzi[k] = gongzi[k] - 1 * f
        print('{}张一元的'.format(int(f)))
        q =int( q + f)
    if gongzi[k]  >= 0.5:
        g = gongzi[k] // 0.5
        gongzi[k] = gongzi[k] - 0.5 * g
        print('{}张五分的'.format(int(g)))
        r = int(r + g)
    if gongzi[k]  >= 0.1:
        h = gongzi[k] // 0.1
        gongzi[k] = gongzi[k] - 0.1 * h
        print('{}张一角的'.format(int(h)))
        s = int(s + h)
    if gongzi[k] >= 0.05:
        i = gongzi[k] // 0.05
        gongzi[k] = gongzi[k] - 0.05 * i
        print('{}张五分的'.format(int(i)))
        t = int(t + i)
    if gongzi[k]  >= 0:
        j = (gongzi[k] + 0.006) // 0.01
        print('{}张一分的'.format(int(j)))
        u = int(u + j)
    print('*******************************************')
print('{}张一百的，{}张五十的,{}张二十的，{}张十块的，{}张五块的，{}张一块的，{}张五角的，{}张一角的,{}张五分的，{}张一分的'.format(l, m, n, o, p, q, r, s, t, u))
