class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.f = lambda x:x == x[::-1]
        result = []
        self.dfs(s,result,[])
        return result
    def dfs(self,s,result,path):
        if not s:
            result.append(path)
        else:
            for i in range(1,len(s)+1):
                if self.f(s[:i]):
                    self.dfs(s[i:],result,path+[s[:i]])
x = Solution()
s = input()
print(len(x.partition(s)))