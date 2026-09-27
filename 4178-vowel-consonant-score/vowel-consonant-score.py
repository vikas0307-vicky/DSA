class Solution(object):
    def vowelConsonantScore(self, s):
        v = c = 0
        for ch in s:
            if ch.isalpha():
                if ch in "aeiou":
                    v += 1
                else:
                    c += 1

        if c > 0:
            return v//c
        else:
            return 0
        