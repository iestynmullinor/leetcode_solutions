"""You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0."""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        best_profit = 0

        for i in range(len(prices)-1):
            buy = prices[i]
            sell = max(prices[i+1:])
            if sell - buy > best_profit:
                best_profit = sell - buy

        return best_profit


