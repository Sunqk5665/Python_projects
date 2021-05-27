# -*- coding: utf-8 -*-

import random
from chinesename import chinesename  # pip install chinesename

# 二分查找函数
def binary_search(lst, uid):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high)//2
        if lst[mid]["uid"] == uid:
            return lst[mid]
        elif lst[mid]["uid"] < uid:
            low = mid + 1
        else:
            high = mid - 1

    return None

# 生成学生信息
def get_students(n):
    """
    @param n: 数量
    @return: {list}
    """

    cn = chinesename.ChineseName()

    uids = list(range(1001, 1001+n))
    lst = []
    for uid in uids:
        dct = {
            "uid": uid,
            "name": cn.getName(),
            "age": random.randint(18, 20)
        }
        lst.append(dct)

    return lst


if __name__ == '__main__':
    students = get_students(100000)

    ret = binary_search(students, 1005)

    print(ret)
