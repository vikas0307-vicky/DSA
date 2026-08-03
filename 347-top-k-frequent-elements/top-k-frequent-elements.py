class Solution(object):
    def topKFrequent(self, nums, k):
        freq = {}

        # Count frequency
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Create buckets
        bucket = [[] for _ in range(len(nums) + 1)]

        # Put numbers into buckets
        for num, count in freq.items():
            bucket[count].append(num)

        ans = []

        # Take elements from highest frequency
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans