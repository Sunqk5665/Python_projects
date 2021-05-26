# 使O(n)尽可能的小，采用二分查找
def F(arr):
    l = 0
    r = len(arr) - 1
    while(l<r):
        mid = (l+r) // 2
        if arr[mid] == mid:
            l = mid + 1
        elif arr[mid] > mid:
            r = mid
    return l

if __name__ == "__main__":
    arr = [int(i) for i in input().split()]
    print(F(arr))