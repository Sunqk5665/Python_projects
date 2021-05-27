class Solution:
    def removeknums(self, nums, k):
        s = []
        nums = list(map(int, nums))
        for i in range(len(nums)):
            number = int(nums[i])
            while len(s) != 0 and s[len(s) - 1] > number and k > 0:
                s.pop(-1)
                k -= 1
            if number != 0 or len(s) != 0:
                s.append(number)
        while len(s) != 0 and k > 0:
            s.pop(-1)
            k -= 1
        result = ""

        result = ''.join(str(i) for i in s)

        return result


if __name__ == "__main__":
    S = Solution()
    print(S.removeknums("1432219", 2))