class Solution(object):
    def mergeAlternately(self, word1, word2):
        s=""
        b=max(len(word1),len(word2))
        a=min(len(word1),len(word2))
        for i in range(a):
            s+=(word1[i])
            s+=(word2[i])
        for i in range(a,b):
            if len(word1)>len(word2):
                s+=word1[i]
            else:
                s+=word2[i]
        return s