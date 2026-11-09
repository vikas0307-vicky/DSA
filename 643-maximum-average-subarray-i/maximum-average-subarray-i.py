class Solution(object):
    def findMaxAverage(self, nums, k):
        if len(nums) == 1:
            return float(nums[0])

        i = 0
        j = k
        avg = 0.0

        for x in range(k):
            avg += float(nums[x]) / k

        max_avg = avg

        while (j < len(nums)):
            avg = avg - float(nums[i]) / k
            avg = avg + float(nums[j]) / k
            max_avg = max(max_avg, avg)
            i = i + 1
            j = j + 1

        return max_avg