class Solution(object):
    def isPalindrome(self, s):
        s1= re.sub(r'[^a-zA-Z0-9]',"", s)
        s1=s1.lower()
        s2=s1[::-1]
        if(s1==s2):
            return True
        else:
            return False
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

        