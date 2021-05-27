class Solution:
    def maxlength(self, nums):
        if len(nums) < 2:
            return len(nums)
        BEGIN = 0
        UP = 1
        DOWN = 2
        STATE = BEGIN
        max_length = 1
        vision = [UP, BEGIN, DOWN]
        for i in range(1, len(nums)):

            if STATE == 0:
                if nums[i - 1] < nums[i]:
                    STATE = 1
                    max_length += 1
                elif nums[i - 1] > nums[i]:
                    STATE = 2
                    max_length += 1
            if STATE == 1:
                if nums[i - 1] > nums[i]:
                    STATE = 2
                    max_length += 1

            if STATE == 2:
                if nums[i - 1] < nums[i]:
                    STATE = 1
                    max_length += 1
        return max_length


if __name__ == "__main__":
    S = Solution()
    g = [1, 17, 5, 10, 13, 15, 10, 5, 16, 8]
    result = S.maxlength(g)
    print(result)