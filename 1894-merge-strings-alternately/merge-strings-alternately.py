class Solution(object):
    def mergeAlternately(self, word1, word2):
        result=""
        for i in range(max(len(word1),len(word2))):
            if i < len(word1):
                result =result + word1[i]

            if i < len(word2):
                result = result + word2[i]

        return ("".join(result))
