class Solution(object):
    def compress(self, c):
        i=0
        j=0
        n=len(c)

        while i<n:
            count = 0
            ch=c[i]

            while i < n and c[i] == ch:
                count += 1
                i = i + 1
            c[j] = ch
            j=j+1

            if count > 1:
                for x in str(count):
                    c[j] = x
                    j = j+1 
        return j



        
        