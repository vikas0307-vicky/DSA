class Solution(object):
    def maxSubArray(self, nums):
        sum = float("-inf")
        total = 0

        for i in nums:
            total = total + i
            if total > sum:
                sum = total
            if total < 0:
                total = 0
        return sum

             



        