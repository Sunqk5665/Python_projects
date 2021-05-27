def RadixSort(a):
    i = 0                                             #初始为个位排序
    n = 1                                           #最小的位数置为1（包含0）
    max_num = max(a)                       #得到带排序数组中最大数
    while max_num > 10**n:              #得到最大数是几位数
        n += 1
    while i < n:
        bucket = {}                             #用字典构建桶
        for x in range(10):
            bucket.setdefault(x, [])    #将每个桶置空
        for x in a:                               #对每一位进行排序
            radix =int((x / (10**i)) % 10)   #得到每位的基数
            bucket[radix].append(x) #将对应的数组元素加入到相应位基数的桶中
        j = 0
        for k in range(10):
            if len(bucket[k]) != 0:       #若桶不为空
                for y in bucket[k]:         #将该桶中每个元素
                    a[j] = y                       #放回到数组中
                    j += 1
        i += 1

if __name__ == '__main__':
    a = [12,3,45,3543,214,1,4553]
    print("Before sorting...")
    print("---------------------------------------------------------------")
    print(a)
    print("---------------------------------------------------------------")
    RadixSort(a)
    print("After sorting...")
    print("---------------------------------------------------------------")
    print(a)
    print("---------------------------------------------------------------")
