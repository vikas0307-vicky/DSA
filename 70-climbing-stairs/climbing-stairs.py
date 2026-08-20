class Solution(object):
    def climbStairs(self, n):
        if n<=2:
            return n
        a,b =1,2
        for i in range(n-2):
            temp =a + b
            a=b
            b=temp
        return b
        