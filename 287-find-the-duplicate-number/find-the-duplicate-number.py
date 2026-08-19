class Solution(object):
    def findDuplicate(self, nums):
        s1= set()
        for i in nums:
            if i in s1:
                return i
            s1.add(i)


                #was is alredy present
                # else: for new entry


  


        

        