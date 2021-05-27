def derivative(coe:list)->list:
    i = len(coe)
    j =1
    newcoe = []
    while j<i:
        newcoe.append(coe[j]*j)
        j=j+1
    return newcoe
def bond(coe:list,s:float)->float:
    i = len(coe)
    bon =0
    while i > 0:
        bon = bon + coe[i - 1] * s ** (i - 1)
        i = i - 1
    return bon

def newton(x:int,coe:list)->int:
    s = x
    i = len(coe)
    d = bond(coe,s)
    while(d>0.00000000000000000000000000000000011):
        list = derivative(coe)
        s = s-(bond(coe,s)/bond(list,s))
        d = bond(coe,s)
        #s=s-(s**2-2*s+1)/(2*s-2)

    return s
#输入要求，输入初始的X0和系数列表，入X^2-2X+1可输入：newton(2,nums) 其中nums=[1,-2,1]
nums=[1,-2,1]
print(newton(2,nums))
