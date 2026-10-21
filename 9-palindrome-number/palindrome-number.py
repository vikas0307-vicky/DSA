# # class Solution(object):
#     def isPalindrome(self, x):
#         x1 = str(x)[::-1]

#         if str(x) == x1:
#             return True
#         else:
#             return False

class Solution(object):
    def isPalindrome(self, x):
        temp = x
        rev = 0 
        while temp > 0:
            r= temp % 10
            temp = temp // 10
            rev = rev * 10
            rev = rev + r
        return rev == x