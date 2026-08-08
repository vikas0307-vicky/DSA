class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        i=0
        ans = 0
        for j in range(len(s)):
            if i < len(g) and s[j] >= g[i]:
                ans=ans+1
                i=i+1
        return ans
