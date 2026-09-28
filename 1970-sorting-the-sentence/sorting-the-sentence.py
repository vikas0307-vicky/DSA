class Solution(object):
    def sortSentence(self, s):
        words = s.split()
        words.sort(key=lambda x: int(x[-1]))
        result = []
        for word in words:
            result.append(word[:-1])

        return " ".join(result)
