def bubble_sort2(collection):
    """
    如果没有元素交换，说明数据在排序过程中已经有序，直接退出循环
    """
    compare_count=0
    length = len(collection)
    for i in range(length-1):
        swapped = False
        print(collection)
        for j in range(length-1-i):
            compare_count+=1
            if collection[j] > collection[j+1]:
                swapped = True
                tmp = collection[j]
                collection[j] = collection[j+1]
                collection[j+1] = tmp
        if not swapped: break  # Stop iteration if the collection is sorted.
    print(f"经历的总循环次数是：{compare_count}")
    return collection
print("排序开始------")
unsorted = [3,4,2,1,5,6,7,8]
print("排序结束------: ",*bubble_sort2(unsorted))