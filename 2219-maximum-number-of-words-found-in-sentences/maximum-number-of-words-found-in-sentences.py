class Solution(object):
    def mostWordsFound(self, a):
        m=0
        for i in a:
            m=max(m,i.count(" ")+1)
        return m
        
            