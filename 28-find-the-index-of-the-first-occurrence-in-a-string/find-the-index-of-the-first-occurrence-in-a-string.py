class Solution(object):
    def strStr(self, haystack, needle):
        m=len(needle)
        n=len(haystack)
        l=n-m+1
        for i in range(l):
            if(haystack[i:i+m]==needle):
                return i
        return -1
        