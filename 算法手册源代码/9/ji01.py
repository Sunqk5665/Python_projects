#coding: utf-8
#!/usr/bin/python
import random
import math

#随机生成0~100之间的数值
def get_andomNumber(num):
    lists=[]
    i=0
    while i<num:
        lists.append(random.randint(0,100))
        i+=1
    return lists


# 头部需导入import math
def radix_sort(lists, radix=10):
    k = int(math.ceil(math.log(max(lists), radix)))
    bucket = [[] for i in range(radix)]
    for i in range(1, k+1):
        for j in lists:
            bucket[int(j/(radix**(i-1)) % (radix**i))].append(j)
        del lists[:]
        for z in bucket:
            lists += z
            del z[:]
    return lists
a = get_andomNumber(10)
print("排序之前：%s" %a)

b = radix_sort(a)

print("排序之后：%s" %b)