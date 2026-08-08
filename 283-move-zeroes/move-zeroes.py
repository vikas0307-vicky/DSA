class Solution(object):
    def moveZeroes(self, nums):
        n = len(nums)
        start = 0
        for i in range(n):
            if nums[i] != 0:
                nums[start],nums[i] = nums[i],nums[start]
                start = start+1
        return nums


        