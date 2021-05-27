
import math  #为了使用cos函数

def takeStep(Xcur):
    Xnex=[0,0,0];
    Xnex[0]=math.cos(Xcur[1]*Xcur[2])/3.0+1.0/6
    Xnex[1]=math.sqrt(Xcur[0]*Xcur[0]+math.sin(Xcur[2])+1.06)/9.0-0.1
    Xnex[2]=-1*math.exp(-1*Xcur[0]*Xcur[1])/20.0-(10*math.pi-3)/60
    return Xnex
    
def initialize():
    X0=[0.1,0.1,-0.1]
    return X0

def ColculateDistance(Xcur,Xnew):
    temp=[Xcur[0]-Xnew[0],Xcur[1]-Xnew[1],Xcur[2]-Xnew[2]]    
    dis=math.sqrt(temp[0]*temp[0]+temp[1]*temp[1]+temp[2]*temp[2])
    return dis
    
def iteration(eps,maxIter):
    cur_eps=10000
    Xcur=initialize()
    Xnew=[0,0,0]
    iterNum=1
    print("--------------------------开始迭代--------------------------")
    print("  迭代次数  |    Xk1    |    Xk2    |    Xk3    |    eps    ")

    while (cur_eps>eps and iterNum<maxIter) :
        Xnew=takeStep(Xcur);
        cur_eps=ColculateDistance(Xcur,Xnew)
        print("     %d       %.8f  %.8f  %.8f  %8.8f"%(iterNum,Xcur[0],Xcur[1],Xcur[2],cur_eps))
        iterNum+=1
        Xcur=Xnew
    return 0
    

iteration(10**-10,200)

 