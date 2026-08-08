class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        n = max(candies)
        ans=[]
        for i in range(len(candies)):
            result  = candies[i] + extraCandies
            if result >= n:
                ans.append(True)
            else:
                ans.append(False)
        return ans          