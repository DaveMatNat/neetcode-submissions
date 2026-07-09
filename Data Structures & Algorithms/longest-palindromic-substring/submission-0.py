class Solution:
    def longestPalindrome(self,s: str) -> str:
        if len(s) == 0:
            return ""
        max_len, idx = 1, (0,0)
        dp = [[False] * len(s) for r in range(len(s))]
        # Base cases
        # 1 char
        for i in range(len(s)):
            dp[i][i] = True

        for i in range(len(s)-1, -1, -1):
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    if i == j-1:
                        dp[i][j] = True
                        if max_len < 2:
                            max_len = 2
                            idx = (i,j)
                    else:
                        dp[i][j] = dp[i+1][j-1]
                        if dp[i][j]:
                            if (j-i+1) > max_len:
                                max_len = j-i+1
                                idx = (i,j)
        # print(s[idx[0]:idx[1]+1])
        # for r in dp:
        #     print(r)
        return s[idx[0]:idx[1]+1]