class Solution(object):
    def removeStars(self, s):
        a=list(s)
        s=[]
        for i in a:
            if i == "*":
                s.pop()
            else:
                s.append(i)

        ans=""
        for i in s:
            ans=ans+i
        return ans