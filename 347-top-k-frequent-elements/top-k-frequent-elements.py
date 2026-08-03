from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):

        count = Counter(nums)
        ret = []
        def get_values(x):
            return count[x]
        count = sorted(count, key=get_values)
        ret = [name for name in count[-k:]]
        return ret