c=[-1,49,38,65,97,76,13,27,49]    #其中[0]=-1这一位置是暂存单元
d=[-1,49,38,65,97,76,13,27,49]

#直接插入排序------------------------------------------------------
def InsertSort(list):
    for i in range(2,len(list)):
        if list[i]<list[i-1]:       #小于的话，需要将list[i]插入有序子表
            list[0]=list[i]         #复制为哨兵
            list[i]=list[i-1]       #先将list[i]前面一元素后移一位
            j=i-2                   #从list[i]前面的前面开始逐一判断
            while list[0]<list[j]:
                list[j+1]=list[j]
                j-=1
            list[j+1]=list[0]       #最后要是不比[j]小，就插在[j+1]处

#折半插入排序------------------------------------------------------
def BinaryInsertSort(list):
    for i in range(2,len(list)):
        list[0]=list[i]
        low=1
        high=i-1
        while low<=high:
            m=int((low+high)/2)         #折半
            if list[0]<list[m]:     #插入点在低半区
                high=m-1
            else:                   #插入点在高半区
                low=m+1
        j=i-1                       #记录后移
        while j>=high+1:
            list[j+1]=list[j]
            j-=1
        list[high+1]=list[0]



InsertSort(c)
print(c[1:])

BinaryInsertSort(d)
print(d[1:])