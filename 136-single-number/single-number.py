class Solution(object):
    def singleNumber(self, nums):
        h={}
        for i in nums:
            if i in h:
                h[i] = h[i]+1

            else:
                h[i] = 1
        for i in h:
            if h[i] == 1:
                return i




        # for i in range(len(nums)):
        #     count = 0
        #     for j in range(len(nums)):
        #         if nums[i] ==nums[j]:
        #             count=count+1

        #     if count == 1:
        #         return(nums[i])



        