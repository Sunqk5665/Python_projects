class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        # 排列组合方法
        if n == 0:
            return 1
        if n == 1:
            return 10
        sum = 10
        # sum = sum + 9*9 + 9*9*8 + 9*9*8*7
        for i in range(2, n + 1):
            sum = sum + self.getvalue(i)
        return sum

    def getvalue(self, n):
        # n >= 2
        result = 9
        for i in range(2, n + 1):
            result = result * (10 - (i - 1))
        return result

n = int(input())
x = Solution()
print(x.countNumbersWithUniqueDigits(n))