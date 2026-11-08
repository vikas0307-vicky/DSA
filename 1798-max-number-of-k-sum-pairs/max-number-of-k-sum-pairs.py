class Solution(object):
    def maxOperations(self, nums, k):
        nums.sort()
        res= 0 
        l = 0
        r = len(nums)-1

        while l < r:
            Sum = nums[l] + nums[r]
            if Sum > k:
                r -= 1
            elif Sum < k:
                l += 1
            else:
                res += 1
                l += 1 
                r -= 1
        return res





        