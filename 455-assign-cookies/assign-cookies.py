class Solution(object):
    def findContentChildren(self, child, cookies):
        child.sort(reverse = True)
        cookies.sort(reverse = True)
        j=0
        ans = 0
        for i in child:
            if j >= len(cookies):
                break
            if cookies[j] >= i:
                ans = ans + 1 
                j=j+1
        return ans