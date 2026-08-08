class Solution(object):
    def findContentChildren(self, child, cookies):
        child.sort(reverse = True)
        cookies.sort(reverse = True)
        j = 0
        res = 0
        for c in child:
            if j >= len(cookies):
                break
            if cookies[j] >= c:
                res += 1
                j += 1
        return res