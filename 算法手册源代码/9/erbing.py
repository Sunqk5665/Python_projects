'''

二路 归并排序 ，Python  实现
MergeSort(array,p,q)

 Merge(array,low,middle,high)  对这个函数进行，对array 进行merge ，就是 把array ，
 前半部分是已经排序，  后半部分已经排序
 把 array  组成一个新的array， Merge 就是把 array 左半部分，和右半部分分别 取出一个值比较，谁小 ，谁就放在arr[] 数组里面，
 最后如果 left_array 有剩余， 直接 copy 到 array[]数组里面；
 left_array 有剩余， 直接 copy 到 array[]数组里面。
'''

def Merge(array, low, middle, high):
    n1 = middle - low + 1
    n2 = high - middle
    left_array = [None]*n1
    right_array = [None]*n2

    # 把array 左边的值，放到left_arr  数组里面
    for i in range(0, n1):
        left_array[i] = array[i + low]

    # 把 array 右边的值，放到 right_arr  数组里面
    for j in range(0, n2):
        right_array[j] = array[j + middle + 1]

    i, j = 0, 0
    k = low
    while i != n1 and j != n2:
        if left_array[i] <= right_array[j]:
            array[k] = left_array[i]
            k += 1
            i += 1
        else:
            array[k] = right_array[j]
            k += 1
            j += 1

    while i < n1:
        array[k] = left_array[i]
        k += 1
        i += 1

    while j < n2:
        array[k] = right_array[j]
        k += 1
        j += 1


def MergeSort(array, p, q):
    if p < q:
        # 转成int  类型
        mid = int((p + q) / 2)
        MergeSort(array, p, mid)
        MergeSort(array, mid + 1, q)
        Merge(array, p, mid, q)


if __name__ == "__main__":
    # mylist=[1,45,56,34,67,88,54,22]
    mylist = [1, 34, 6, 21, 98, 31, 7, 4, 56, 59, 27, 13, 36, 47, 67, 37, 25, 2]

    length = len(mylist)
    MergeSort(mylist, 0, length - 1);

    print(mylist)