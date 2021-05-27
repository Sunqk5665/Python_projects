def f(xi):
    return xi*xi*xi-xi-1
def f1(xi):
    return 3*xi*xi-1
x=[]
x.append(0.5)
eps=1e-14     #误差限制
error=abs(f(x[-1]))    #最新加的x在最后
number_iteration=0
while error>eps:
    x.append(x[-1]-f(x[-1])/f1(x[-1]))  #x k+1
    error=abs(f(x[-1]))
    number_iteration=number_iteration+1
print('牛顿法迭代次数为%f次'%(number_iteration)) #格式化输出
print('方程的根x*为%f'%(x[-1]))
print('f(x*)的值为%f'%(f(x[-1])))
