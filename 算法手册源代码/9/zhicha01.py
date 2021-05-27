#升序排列
def Zhijie_Px(arr):

    for i in range(1,len(arr)):
        if arr[i]<arr[i-1]:
            temp=arr[i]
            j=i-1
            while arr[j]>temp and j>=0:
                arr[j+1]=arr[j]
                j -=1
            arr[j+1]=temp
    print(arr)

#降序排列
def Zhijie_Px2(arr):
    for i in range(1,len(arr)):
        if arr[i]>arr[i-1]:
            temp=arr[i]
            j=i-1
            while arr[j]<temp and j>=0:
                arr[j+1]=arr[j]
                j -=1
            arr[j+1]=temp
    # arr=arr[::-1]
    print(arr)

Zhijie_Px([88,78,65,156,239,43])

Zhijie_Px2([88,78,65,156,239,43])

