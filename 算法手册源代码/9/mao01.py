def bubble_sort(collection):
    """
    无任何优化版
    """
    compare_count = 0
    length = len(collection)
    for i in range(length - 1):
        print(collection)  # 方便查看数组的排序过程
        for j in range(length - 1 - i):
            compare_count += 1
            if collection[j] > collection[j + 1]:
                tmp = collection[j]
                collection[j] = collection[j + 1]
                collection[j + 1] = tmp
    print(f"经历的总循环次数是：{compare_count}")
    return collection

print("排序开始------")
unsorted = [3,4,2,1,5,6,7,8]
print("排序结束------: ",*bubble_sort(unsorted))