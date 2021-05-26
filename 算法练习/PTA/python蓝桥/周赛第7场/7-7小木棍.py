def hanshu(n):
    a = list(map(int, input().split()))
    a.sort()
    count = 0
    if(n<3):
        return 0
    for i in range(n-1,1,-1):
        left = 0  # 左指针
        right = i-1 # 右指针
        while(left < right):
            if((a[left] + a[right]) > a[i]):
                count = count + (right-left)
                right -= 1
            else:
                left += 1
    return count

n = int(input())

print(hanshu(n))

