class Solution(object):
    def finalValueAfterOperations(self, operations):
        ans = 0
        for i in operations:
            if i=="++X" or i=="X++":
                ans += 1
            else:
                ans -=1
        return ans
