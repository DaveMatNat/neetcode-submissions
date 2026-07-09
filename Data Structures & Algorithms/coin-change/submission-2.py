class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [100001] * (amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            for d in coins:
                if i-d >= 0:
                    dp[i] = min(dp[i], 1 + dp[i-d])
        return -1 if dp[amount] > 10000 else dp[amount]

        # Top-down
