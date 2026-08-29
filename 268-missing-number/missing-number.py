class Solution(object):
    def missingNumber(self, nums):

        # n =nums.sort()
        # for i in range(len(nums)):
        #     if nums[i] != i:
        #         return i

        # return len(nums)


        sum1 = sum(nums)
        n = len(nums)
        x = n*(n+1)//2
        return x - sum1


        