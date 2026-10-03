class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        maximum = max(candies)

        return [candy + extraCandies >= maximum for candy in candies]