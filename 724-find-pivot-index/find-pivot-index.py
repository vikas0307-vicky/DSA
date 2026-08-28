class Solution(object):
    def pivotIndex(self, nums):
        sum1=0
        l1=[]
        for i in nums:
            sum1 =sum1+i
            l1.append(sum1)
   

        sum2=0
        l2=[]
        for i in range(len(nums)-1,-1,-1):
            sum2 = sum2 + nums[i]
            l2.append(sum2)



        l2.reverse()
        

        for i in range(len(nums)):
            if l1[i] == l2[i]:
                print(i)
                return i


        return -1
        