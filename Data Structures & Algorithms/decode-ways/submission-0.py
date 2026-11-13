class Solution:
    def numDecodings(self, s: str) -> int:
        mapping = {i-65+1: chr(i) for i in range(65, 65+26)}
        
        # Two case from the back --> 1 num, or 2 num (only up to 26 tho)
        digits = len(s)
        # dp[i] = total ways to decode first i digits
        dp = [0] * (digits+1)

        # Base case
        dp[0] = 1

        res = []

        for i in range(1, digits+1):
            # two cases
            # 1) i + total ways for [i-1] digits
            # 2) i and i-1 + total ways for [i-2] digits (only if str(s[i-2]+s[i-1]) <= 26) also leading zero is a problem
            print(f"----{i}-----")
            # Case 1
            # print("Case 1: ", s[i-1])
            # print("Before last: ", list(s[:i-1]))
            dp[i] = dp[i-1] if s[i-1] != '0' else 0
            # print(dp)

            # Case 2
            if (i-2) >= 0:
                back_two = int(s[i-2])*10 + int(s[i-1])

                # print("\nCase 2: ", str(back_two))
                # print("Before last two: ", list(s[:i-2]))
                if (10 <= back_two <= 26):
                    dp[i] += dp[i-2]  
            print(dp)
            print("\n")
        return dp[-1]