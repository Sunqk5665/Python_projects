#coding=gbk;
from sympy import *;
from future import *;
import math;
import sys;
x=symbols("x");
#f=x*exp(x)-1;  #这个地方的表达式可以根据需要进行更改
#注意到这里，就是先将f对x进行不定积分，然后再求导。
#因为一开始input时候f也不过就是个表达式
f=input("请输入方程的表达式：");
f=integrate(f, x);
f=diff(f);

list_in=input("请输入初始值x,极小值sigma以及想要计算的次数: ").split(" ");
x0=float(list_in[0]);
sigma=float(list_in[1]);
N=int(list_in[2]);

if diff(f).subs(x,x0)==0:
    print(x0)
    sys.exit();
account=1;
x_new=x0;
while account<=N:
    x_new=x0-f.subs(x,x0)/diff(f).subs(x,x0);
        #x_new=float(x_new);
    if math.fabs(x_new-x0)<sigma:
        print(x_new)
        sys.exit();
    x0=x_new;
    account+=1;
print("无法解出，不满足条件")
