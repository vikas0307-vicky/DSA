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


class Solution:
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        x = abs(x)

        rev = 0

        while x:
            rev = rev * 10 + x % 10
            x //= 10

        rev *= sign

        return rev if -2**31 <= rev <= 2**31 - 1 else 0