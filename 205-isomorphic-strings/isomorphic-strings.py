class Solution:
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False

        s1={}
        t1={}
        
        i = 0
        while i<len(s):
            a=s[i]
            b=t[i]

            if a in s1 and s1[a] != b:
                return False
            
            if b in t1  and t1[b] != a:
                return False

            s1[a] = b
            t1[b] = a

            i = i + 1
        return True

    