# -*- coding: utf-8 -*-

import time

# 计时装饰器
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        end = time.time()
        print("time: %s"% (end-start))
        return ret
    return wrapper


# 顺序（线性）查找 O(n)
@timer
def line_search(lst, val):
    for index, value in enumerate(lst):
        if val == value:
            return index

    return None

# 二分查找(需要有序) O(logn)
@timer
def binary_search(lst, val):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (high + low)//2
        if lst[mid] == val:
            return mid
        elif lst[mid] < val:
            low = mid + 1
        else:
            high = mid - 1

    return None


if __name__ == '__main__':
    lst = list(range(100000))

    ret = line_search(lst, 90000)
    print(ret)


    ret = binary_search(lst, 90000)
    print(ret)

