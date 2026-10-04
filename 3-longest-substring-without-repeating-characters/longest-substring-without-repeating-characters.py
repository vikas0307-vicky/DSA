class Solution:
    def lengthOfLongestSubstring(self, s):
        last_seen = {}  # character -> last index where we saw it
        left = 0
        best = 0

        for right, ch in enumerate(s):
            # if ch is already inside the current window, jump left past it
            if ch in last_seen and last_seen[ch] >= left:
                left = last_seen[ch] + 1

            last_seen[ch] = right
            best = max(best, right - left + 1)

        return best