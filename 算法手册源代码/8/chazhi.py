# 时间复杂度O(log(n))

def binary_search(lis, key):
    low = 0
    high = len(lis) - 1
    time = 0
    while low < high:
        time += 1
        # 计算mid值是插值算法的核心代码
        mid = low + int((high - low) * (key - lis[low])/(lis[high] - lis[low]))
        print("mid=%s, low=%s, high=%s" % (mid, low, high))
        if key < lis[mid]:
            high = mid - 1
        elif key > lis[mid]:
            low = mid + 1
        else:
            # 打印查找的次数
            print("times: %s" % time)
            return mid
    print("times: %s" % time)
    return False

if __name__ == '__main__':
    LIST = [1, 5, 7, 8, 22, 54, 99, 123, 200, 222, 444]
    result = binary_search(LIST, 444)
    print(result)