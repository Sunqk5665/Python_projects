def quicksort(array):
    if len(array) < 2:
        return array  # 基线条件：为空或者只包含一个元素的数组是“有序”的
    else:
        pivot = array[0]  # 选择基准值

        less = [i for i in array[1:] if i <= pivot]#由所有小于或者等于基准值的元素组成的子数组
        greater = [i for i in array[1:] if i > pivot]#由所有大于基准值的元素组成的子数组
        return  quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([2, 7, 1, 3, 4, 8, 2]))
# print([1,2,3]+[4,5,6])