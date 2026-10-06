class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # so this is true if the distribution of the letters is the same *in the same order*
        # the same amount of 1s, 2s, 3s, etc. of letters

        # count the number of each letter

        if len(s) != len(t):
            return False

        mappings = {}
        reverse = {}

        for i in range(len(s)):
            if s[i] in mappings:
                if t[i] != mappings[s[i]]:
                    return False
            else:
                if t[i] in reverse:
                    return False

                mappings[s[i]] = t[i]
                reverse[t[i]] = s[i]

        return True