import numpy as np
n = list(input())
arr = input("")
nums = [int(i) for i in arr.split()]
#排序
nums.sort()

#address = nums[n>>1]
address = np.median(nums)
res = 0
for num in nums:
    res += abs(num - address)
print(res)