class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        shortest = min(len(s) for s in strs)
        for i in range(shortest):
            for j in range(len(strs)-1):
                if strs[j][i] != strs[j+1][i]:
                    return res 
            res += strs[0][i]
        return res
