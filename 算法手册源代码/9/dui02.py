'''堆排序'''
'''1.从下至上，从右至左，对每个节点进行调整，以得到一个大顶堆'''
'''2.首尾互换，尾部元素已是有序序列，堆元素个数减1，此部分仍为无序序列，继续调整'''


def big_endian(arr, start, end):
    root = start
    while True:
        child = root * 2 + 1
        if child > end:
            break
        if child + 1 <= end and arr[child] < arr[child + 1]:
            child += 1
        if arr[root] < arr[child]:
            arr[root], arr[child] = arr[child], arr[root]
            root = child
        else:
            break


def heap_sort(arr):
    first = len(arr) // 2 - 1
    for start in range(first, -1, -1):
        big_endian(arr, start, len(arr) - 1)
    for end in range(len(arr) - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        big_endian(arr, 0, end - 1)


def main():
    l = [3, 1, 4, 9, 6, 7, 5, 8, 2, 10]
    print(l)
    heap_sort(l)
    print(l)


if __name__ == "__main__":
    main()