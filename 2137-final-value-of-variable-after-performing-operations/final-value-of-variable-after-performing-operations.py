class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        ans=0
        for s in operations:
            if s=="++X" or s=="X++":
                ans+=1
            else:
                ans-=1
        return ans
        