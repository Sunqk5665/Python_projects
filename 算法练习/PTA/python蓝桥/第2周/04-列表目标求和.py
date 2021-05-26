# 使用枚举的方法，拿到列表的一个数字，计算出与target的差值，
# 如果差值在列表中，并且下标不是数字本身，就返回两个数字的下标。
def twosum(nums,target):
    l = len(nums)
    for i in range(l):
        another = target - nums[i]
        if another in nums:
            j = nums.index(another)
            if i==j:     # 若两个数是同一个数则 continue
                continue
            else:
                return[i,j]

if __name__=='__main__':
    nums = eval(input())
    target = int(input())
    print(twosum(nums,target),end="")
