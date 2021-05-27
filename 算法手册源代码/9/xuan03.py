#待排序数组arr，排序方式order>0升序，order<0降序
def selectSort(arr,order):
    rborder = len(arr)
    for i in range(0,rborder):
        p = i
        j = i+1
        while(j<rborder):
            if((arr[p]>arr[j]) and (int(order)>0)) or ((arr[p]<arr[j]) and (int(order)<0)):
                p = j
            j += 1
        arr[i], arr[p] = arr[p], arr[i]
        i += 1
    return arr

A = [64, 25, 12, 22, 11]
print(selectSort(A, -1))
print(selectSort(A, 1))