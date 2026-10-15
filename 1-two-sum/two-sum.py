class Solution(object):
    def twoSum(self, nums, target):
        n=len(nums)
        d={}
        for i in range(n):
            r = target - nums[i]
            if r in d:
                return d[r],i
            d[nums[i]] = i
 
        