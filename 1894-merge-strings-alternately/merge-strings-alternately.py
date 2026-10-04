class Solution(object):
    def mergeAlternately(self, word1, word2):
        x = word1 if (len(word1) < len(word2)) else word2
        y = word1 if len(word1) > len(word2) else word2
        final = []
        for i in range(len(x)):
            final.append(word1[i])
            final.append(word2[i])
        final.append(y[len(x):])
        return "".join(final)
        # result = []

        # for i in range(max(len(word1), len(word2))):
        #     if i < len(word1):
        #         result.append(word1[i])

        #     if i < len(word2):
        #         result.append(word2[i])

        # return ''.join(result)