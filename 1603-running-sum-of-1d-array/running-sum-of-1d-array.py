class Solution(object):
    def runningSum(self, nums):
        presum=[0 for i in range(len(nums))]
        sum = 0
        for i in range(len(nums)):
            sum = sum+nums[i]
            presum[i] = sum
        return presum
        



        