class Solution(object):
    def maxProfit(self, prices):
        buy = prices[0]
        profit = 0
        for p in prices:
            if p < buy:
                buy = p
            elif p - buy > profit:
                profit = p -buy
        return profit

