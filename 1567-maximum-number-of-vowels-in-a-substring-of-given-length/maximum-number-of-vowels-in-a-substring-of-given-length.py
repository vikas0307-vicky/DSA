# class Solution:
#     def maxVowels(self, s, k):
#         vowelCount = 0

#         for i in range(k):
#             if s[i] in "aeiou":
#                 vowelCount += 1

#         maxVowelCount = vowelCount

#         for i in range(1, len(s) - k + 1):
#             if s[i - 1] in "aeiou":
#                 vowelCount -= 1

#             if s[i + k - 1] in "aeiou":
#                 vowelCount += 1

#             maxVowelCount = max(maxVowelCount, vowelCount)

#         return maxVowelCount
class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        len_s = len(s)
        if k > len_s:
            return 0
        vowels = set('aeiouAEIOU')
        # s_list = list(s)

        max_window_vowels = len([v for v in s[:k] if v in vowels])
        current_window_vowels = max_window_vowels
        if max_window_vowels == k:
            return k
        
        for i in range(len_s-k):
            if s[i+k] in vowels:
                current_window_vowels += 1
            if s[i] in vowels:
                current_window_vowels -= 1
            if current_window_vowels > max_window_vowels:
                max_window_vowels = current_window_vowels

        return max_window_vowels