# class Solution(object):
#     def reverse(self, x):
#         sign = -1 if x < 0 else 1
#         x = abs(x)

#         rev = 0
#         while(x!=0):
#             r = x%10
#             x = x // 10
#             rev =rev * 10
#             rev = rev + r
#         rev = rev * sign
#         if rev < -2**31 or rev > 2**31 - 1:
#             return 0
#         return(rev)

        
class Solution(object):
    def reverse(self, x):
        s = str(x)

        if x < 0:
            s = s[1:]
            s = s[::-1]
            s = int(s)
            s = -s
        else:
            s = s[::-1]
            s = int(s)

        if -2147483648 <= s <= 2147483647:
            return s
        else:
            return 0