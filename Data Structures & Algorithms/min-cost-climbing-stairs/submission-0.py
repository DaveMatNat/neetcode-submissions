class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp[i] = min cost to past the first i indexes

        dp = [0] * (len(cost)+1)
    

        for i in range(2, len(cost)+1):
            dp[i] = min(cost[i-1] + dp[i-1], cost[i-2]+ dp[i-2])
        return dp[-1]
