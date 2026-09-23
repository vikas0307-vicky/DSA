class Solution(object):
    def sortedSquares(self, nums):
        n = len(nums)
        result = [0] * n
        left = 0
        right = n-1
        k = n-1

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result[k] = nums[left]**2
                left =left + 1
            else:
                result[k] = nums[right]**2
                right = right - 1
            k = k - 1
        return result

        