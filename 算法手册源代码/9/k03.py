def quick_sort(list1, start, end):
    # 递归的退出条件
    if start >= end:
        return
    # 设置起始元素为要寻找位置的基准元素
    mid = list1[start]
    # left为序列左边的由左向右移动的游标
    left = start
    # right为序列右边的由右向左移动的游标
    right = end
    while left < right:
        # 如果left和right未重合，right指向的元素不比基准元素小，
        # 则right向左移动
        while left < right and list1[right] >= mid:
            right -= 1
        # 将right指向的元素放到left的位置上
        list1[left] = list1[right]
        # 如果left于right未重合，left指向的元素比基准元素小
        # 则left向右移动
        while left < right and list1[left] < mid:
            left += 1
        # 将left指向的元素放到right的位置上
        list1[right] = list1[left]

    # 退出循环后，left与right重合，此时所指位置为基准元素的正确位置
    # 将基准元素放到该位置
    list1[left] = mid
    # 对基准元素左边的子序列进行快速排序
    quick_sort(list1, start, left-1)
    # 对基准元素右边的子序列进行快速排序
    quick_sort(list1, left+1, end)


li = [23, 94, 2, 21, 56, 6]
quick_sort(li, 0, len(li)-1)
print(li)

