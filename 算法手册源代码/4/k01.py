def quicksort(num, low, high):  # 快速排序
    if low < high:
        location = partition(num, low, high)
        quicksort(num, low, location - 1)
        quicksort(num, location + 1, high)


def partition(num, low, high):
    pivot = num[low]
    while (low < high):
        while (low < high and num[high] > pivot):
            high -= 1
        while (low < high and num[low] < pivot):
            low += 1
        temp = num[low]
        num[low] = num[high]
        num[high] = temp
    num[low] = pivot
    return low


def findkth(num, low, high, k):  # 找到数组里第k个数
    index = partition(num, low, high)
    if index == k: return num[index]
    if index < k:
        return findkth(num, index + 1, high, k)
    else:
        return findkth(num, low, index - 1, k)


pai = [2, 3, 1, 5, 4, 6]
# quicksort(pai, 0, len(pai) - 1)

print(findkth(pai, 0, len(pai) - 1, 5))