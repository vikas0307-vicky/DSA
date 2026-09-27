class Solution(object):
    def trimTrailingVowels(self, s):
        # return s.rstrip("aeiou")
        v = {"a","e","i","o","u"}
        while len(s)>0:
            if s[-1] in v:
                s = s[:-1]
            else:
                break
        return s
        