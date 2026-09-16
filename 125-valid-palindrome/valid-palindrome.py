class Solution(object):
    def isPalindrome(self, s):
        # ans = ""
        # for i in s:
        #     if i.isalnum():
        #         ans = ans+i.lower()
        # return ans == ans[::-1] 
        ans = []
        for i in s:
            if i.isalnum():
                ans.append(i.lower())
        return ans == ans[::-1]

        