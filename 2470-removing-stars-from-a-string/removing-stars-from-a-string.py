class Solution(object):
    def removeStars(self, s):
        skip=0
        res=[]
        for i in reversed(s):
            if i == "*":
                skip+=1
            elif skip:
                skip-=1
            else:
                res.append(i)
        res=reversed(res)
        return "".join(res)