def newtons(f,df,x0,e):
    xn = float(x0)
    e_tmp = e+1
    loop = 1
    while e_tmp>e:
        print('########loop'+str(loop))
        k = df(xn)
        xm = f(xn)
        print('xn='+str(xn)+',k='+str(k)+',y='+str(xm))
        q = xm/k
        xn = xn-q
        e_tmp = abs(0-f(xn))
        print('new xn='+str(xn)+',e='+str(e_tmp)+',q='+str(q))
        loop=loop+1
    return xn


def f(x):
    return x ** 2 + 2 * x


def df(x):
    return 2 * x + 2


x = newtons(f, df, 3, 0.01)
print('the point you find is ' + str(x))
