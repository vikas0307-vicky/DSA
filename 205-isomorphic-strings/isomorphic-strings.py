class Solution(object):
    def isIsomorphic(self, s, t):
        s1={}
        t1={}
        for i in range(len(s)):
            a=s[i]
            b=t[i]

            if a in s1 and s1[a] != b:
                return False
            
            if b in t1 and t1[b] != a:
                return False

            s1[a]= b
            t1[b]= a
        return True

        