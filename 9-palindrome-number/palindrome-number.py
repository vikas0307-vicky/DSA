# # class Solution(object):
#     def isPalindrome(self, x):
#         x1 = str(x)[::-1]

#         if str(x) == x1:
#             return True
#         else:
#             return False

class Solution(object):
    def isPalindrome(self, x):
        rev = str(x)[::-1]

        if str(x) == rev:
            return True
        else:
            return False 