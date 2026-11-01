class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        i = 0
        j= 1
        size = len(flowerbed)
        count = 0
        while j<=size:
            if j==size:
                if flowerbed[i]==0 and flowerbed[i-1]==0:
                    count+=1
                break
            if flowerbed[i]==0:
                if flowerbed[j]==0:
                    count+=1
                    i+=2
                    j+=2
                else:
                    i+=3
                    j+=3
            else:
                i+=2
                j+=2

        return count >= n