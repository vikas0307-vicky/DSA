# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         n =len(s)

#         if n==0:
#             return 0

#         ans = 1
#         set1 = set({})
#         set1.add(s[0])

#         i = 0
#         j = 1

#         while j<n:
#             while s[j] in set1:
#                 set1.discard(s[i])
#                 i=i+1
#             set1.add(s[j])
#             j+=1
#             ans =max(ans,(j-i))

#         return ans


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        distinct = len(set(s))
        last = [-1] * 128
        start = best = 0
        for i, c in enumerate(s):
            code = ord(c)
            if last[code] >= start:
                start = last[code] + 1
                if best >= n - start:
                    break
            last[code] = i
            if i - start + 1 > best:
                best = i - start + 1
                if best == distinct:
                    break
        return best
        

