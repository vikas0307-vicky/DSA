class Solution(object):
    def isBalanced(self, num):
        even_sum = 0
        odd_sum = 0
        leg= len(num)
        for i in range(leg):
            if i % 2 == 0:
                even_sum = even_sum + int(num[i])
            else:
                odd_sum = odd_sum + int(num[i])
        return even_sum == odd_sum