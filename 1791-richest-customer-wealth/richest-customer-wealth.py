class Solution(object):
    def maximumWealth(self, a):
        ans = 0
        for i in a:
            ans = max(ans,sum(i))
        return ans


        