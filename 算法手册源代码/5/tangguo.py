class Solution:
    def findContentChild(self,g,s):
        g = sorted(g)
        s = sorted(s)
        child = 0
        cookie = 0
        while child < len(g) and cookie < len(s):
            if g[child] <= s[cookie]:
                child +=1
            cookie+=1
        return child
if __name__ =="__main__":
    g = [5,10,2,9,15,9]
    s = [6,1,20,3,8]
    S = Solution()
    result = S.findContentChild(g,s)
    print(result)