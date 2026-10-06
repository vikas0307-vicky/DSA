class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split()

        if len(pattern) != len(words):
            return False 

        c={}
        w={}

        for i,j in zip(pattern, words):

            if i in c and c[i] != j:
                return False
            
            if j in w and w[j] != i:
                return False

            c[i] = j
            w[j] = i
        return True
        