from pylab import *

def FibonacciSearch(data, length, key):
    F = [0,1]
    count = 1;
    low = 0
    high = length-1
    if(key < data[low] or key>data[high]):                      #索引超出范围返回错误
        print("Error!!! The ", key, " is not in the data!!!")
        return -1

    data = list(data)
    while F[count] < length:                    #生成斐波那契数列
        F.append(F[count-1] + F[count])
        count = count + 1
    low = F[0]
    high = F[count]

    while length-1 < F[count-1]:                #将数据个数补全
        data.append(data[length-1])
        length = length + 1
    data = array(data)
    while(low<=high):
        mid = low+F[count-1]                    #计算当前分割下标
        if(data[mid] > key):                    #若查找记录小于当前分割记录
            high = mid-1                        #调整分割记录
            count = count-1
        elif(data[mid] < key):                  #若查找记录大于当前分割记录
            low = mid+1
            count = count-2
        else:                                   #若查找记录等于当前分割记录
            return mid
    if(data[mid] != key):                                       #数据key不在查询列表data中返回错误
        print("Error!!! The ", key, " is not in the data!!!")
        return -1

length = 11

data = array([0,1,16,24,35,48,59,62,73,88,99])
key = 35
idx = FibonacciSearch(data, length, key)
print(data)
print("The ", key, " is the ", idx+1, "th value of the data.")