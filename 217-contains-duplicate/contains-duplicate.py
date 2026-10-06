class Solution(object):
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))
        # ans= {}
        # for i in range(len(nums)):
        #     if nums[i] in ans:
        #         return True
        #     ans[nums[i]] = 1
        # return False
            
        
        
