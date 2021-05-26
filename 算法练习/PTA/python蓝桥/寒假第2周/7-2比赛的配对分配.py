class Solution:
    def numberOfMatches(self, n: int) -> int:
        res = 0
        while n != 1:
            if n % 2 == 0:
                res += n // 2
                n //= 2
            else:
                res += n // 2
                n = (n+1) // 2
        return res
n = input()
x = Solution()
print(x.numberOfMatches(int(n)))