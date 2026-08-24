class Solution(object):
    def findDuplicate(self, nums):
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]==nums[j]:
        #             return nums[i]
        s1= set()
        for i in nums:
            if i in s1:
                return i
            s1.add(i)


                #was is alredy present
                # else: for new entry


  


        

        