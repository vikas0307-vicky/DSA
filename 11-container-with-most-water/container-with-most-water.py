class Solution(object):
    def maxArea(self,a):
        i = 0 
        j = len(a)-1
        res = 0
        
        while i < j:
            res = max(res, (j-i) * min(a[i],a[j]))
            if a[i] < a[j]:
                i += 1
            else:
                j -= 1

        return res