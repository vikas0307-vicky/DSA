class Solution(object):
    def findDifference(self, nums1, nums2):



        set1, set2 = set(nums1), set(nums2)
        return [list(set1 - set2), list(set2 - set1)]

        # l1=[]
        # l2=[]
        # for i in nums1:
        #     if i not in nums2 and i not in l1:
        #         l1.append(i)

        # for i in nums2:
        #     if i not in nums1 and i not in l2:
        #         l2.append(i)

        # return [l1,l2] 




        