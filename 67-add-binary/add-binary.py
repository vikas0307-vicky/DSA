class Solution(object):
    def addBinary(self, a, b):
        # binary = bin(int(a,2)+ int(b,2))[2:]
        # return binary
        
        # binary = bin(int(a,2)+ int(b,2))[2:]
        # return binary
        i = len(a)-1
        j = len(b)-1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            total = carry

            if i>= 0:
                total = total + int(a[i])
                i = i - 1
            
            if j>=0:
                total = total + int(b[j])
                j = j - 1

            result.append(str(total % 2))
            carry = total // 2

        return "".join(result[::-1])

