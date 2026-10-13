class Solution(object):
    def maxSubArray(self, nums):

        sum = float("-inf")
        t = 0
        for i in nums:
            t = t + i
            if t > sum:
                sum = t
            if t < 0:
                t = 0
        return sum
                

             



        