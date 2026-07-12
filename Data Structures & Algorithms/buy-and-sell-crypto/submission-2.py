class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        # dp[i] = max prof selling on the first i days
        # dp = [0] * len(prices)
        maxProfit = 0
        for i in range(1, len(prices)):
            # on the ith day, choose to sell or not sell on the ith day
            maxProfit = max(prices[i] - minPrice, maxProfit)
            minPrice = min(minPrice, prices[i])
        return maxProfit