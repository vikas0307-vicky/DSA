class Solution(object):
    def hammingWeight(self, n):
        count = 0
        x = bin(n)

        for i in x:
            if i == '1':
                count = count + 1
        return count        
        