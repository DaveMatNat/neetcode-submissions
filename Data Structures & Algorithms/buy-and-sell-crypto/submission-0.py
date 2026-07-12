class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        for buy in range(len(prices)):
            for sell in range(buy+1, len(prices)):
                maxProf = max(maxProf, prices[sell]-prices[buy])
        return maxProf