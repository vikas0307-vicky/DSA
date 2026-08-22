class Solution(object):
    def checkDivisibility(self, n):

        original = n
        sum1 = 0
        product1 = 1

        while n > 0:
            digit = n % 10
            sum1 = sum1 + digit
            product1 = product1* digit
            n //= 10

        return original % (sum1 + product1) == 0
        