#coding=gbk;
from sympy import *;
from future import *;
import math;
import sys;
x=symbols("x");
#f=x*exp(x)-1;  #����ط��ı��ʽ���Ը�����Ҫ���и���
#ע�⵽��������Ƚ�f��x���в������֣�Ȼ�����󵼡�
#��Ϊһ��ʼinputʱ��fҲ�������Ǹ����ʽ
f=input("�����뷽�̵ı��ʽ��");
f=integrate(f, x);
f=diff(f);

list_in=input("�������ʼֵx,��Сֵsigma�Լ���Ҫ����Ĵ���: ").split(" ");
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
print("�޷����������������")
