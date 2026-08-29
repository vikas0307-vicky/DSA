class Solution(object):
    def missingNumber(self, nums):
        sum1 = sum(nums)
        n = len(nums)
        x = n*(n+1)//2
        return x - sum1
    


        