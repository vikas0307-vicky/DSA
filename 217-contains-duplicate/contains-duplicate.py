class Solution(object):
    def containsDuplicate(self, nums):
        ans= {}
        for i in range(len(nums)):
            if nums[i] in ans:
                return True
            ans[nums[i]] = 1
        return False
            
        
