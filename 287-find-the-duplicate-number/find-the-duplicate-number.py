class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        h={}
        for i in nums:
            if (i in h.keys()):
                return i
            else:
                h[i]=0
        