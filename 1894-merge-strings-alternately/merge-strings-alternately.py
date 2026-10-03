class Solution(object):
    def mergeAlternately(self, word1, word2):
        new = ""
        maxie = max(len(word1),len(word2))
        for i in range((maxie)):
            if i < len(word1):
                new+=word1[i]
            if i < len(word2):
                new+=word2[i]
        return new





        # result=""
        # for i in range(max(len(word1),len(word2))):
        #     if i < len(word1):
        #         result =result + word1[i]

        #     if i < len(word2):
        #         result = result + word2[i]

        # return ("".join(result))
