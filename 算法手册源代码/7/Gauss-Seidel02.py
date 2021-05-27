#Gauss Seidel迭代法
import numpy as np
A=[[10,3,1], [2,-10,3], [1,3,10]]
b=[[14,-5,14]]

def get_base(A):#获得一个基
    base=list(np.zeros((len(A),len(A))))
    D=[]
    for i in base:
        D.append(list(i))
    return D

def get_U(A):#获得U
    D=get_base(A)
    i=0
    while i<len(A):
        k=i+1
        while k<len(A):
            D[i][k]=-A[i][k]
            k=k+1
        i=i+1
    return D

def get_DL(A,U):#获得D-L
    AA=np.array(A)
    UU=np.array(U)
    DDLL=AA+UU
    DL=[]
    for i in DDLL:
        DL.append(list(i))
    return DL

def get_DL_I(DL):#获得D-L的逆
    DL1=np.mat(DL)
    DL2=DL1.I
    return DL2

def get_B(DLI,U):#获得B
    U1=np.mat(U)
    B=DLI*U1
    return B

def get_f(DLI,b):#获得f
    b1=np.mat(b)
    f=DLI*b1.T
    return f

def matrix_to_list(x):
    d=[]
    ans=[]
    for i in x:
        d.append(i.tolist())
    for i in d:
        ans.append(i[0])
    return ans

def roll(A,b,x0):#主循环结构
    U=get_U(A)
    DL=get_DL(A,U)
    DLI=get_DL_I(DL)
    B=get_B(DLI,U)
    f=get_f(DLI,b)
    x=np.mat(x0).T
    y=B*x+f
    return matrix_to_list(y.T)

def main(A,b,x0,e):#输入系数矩阵，方程组右端b，初始值x0，以及需要的绝对误差限
    n=0
    ans=[]
    ans.append(x1)
    ans.append(x0)
    ans1=[]
    ans1.append(x1[0])
    ans1.append(x0[0])
    while abs(ans[-1][0][1]-ans[-2][0][1])>e:
        n=n+1
        x0=roll(A,b,x0)
        ans.append(x0)
    for i in ans:
        ans1.append(i[0])
    return ans1,len(ans1)-2

x1=[[1,1,2]]
x0= roll(A,b,x1)
e=0.00001
print(main(A,b,x0,e))
