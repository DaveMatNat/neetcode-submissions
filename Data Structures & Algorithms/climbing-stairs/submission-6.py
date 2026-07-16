class Solution:
    def climbStairs(self, n: int) -> int:
        # dp[i] = total ways to climb the first i stairs
        dp = [0] * (n+1)
        
        # base cases
        dp[1] = 1 # 1 way -> climb 1
        if n < 2:
            return dp[-1]
            
        dp[2] = 2 # 2 ways -> climb 1+1, or 2

        # recursive case
        for s in range(3,n+1):
            dp[s] = dp[s-1] + dp[s-2] #choices --> 1 step from dp[s-1] |OR| 2 steps from dp[s-2]
        return dp[-1]