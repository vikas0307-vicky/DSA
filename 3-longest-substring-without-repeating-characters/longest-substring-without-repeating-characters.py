class Solution(object):
    def lengthOfLongestSubstring(self, s):
        
        if (len(s) <= 1):
            return len(s)

        substring = s[0]
        right = 0
        longest = 1
        while (right < len(s) - 1):
            right += 1
            if s[right] in substring:
                substring = substring[substring.index(s[right])+1:] + s[right]
            else:
                substring = substring + s[right]
            
            if (longest < len(substring)):
                longest = len(substring)
        return longest