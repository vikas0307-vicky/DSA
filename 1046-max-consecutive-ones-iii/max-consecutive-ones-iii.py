class Solution(object):
    def longestOnes(self, nums, k):
        zeroes = 0
        l = 0
        for r , n in enumerate(nums):
            zeroes += n == 0
            if zeroes > k:
                zeroes -= nums[l] == 0
                l += 1
        return r - l + 1


        