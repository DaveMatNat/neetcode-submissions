class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        collection = set()

        for r in range(len(s)):
            while s[r] in collection:
                collection.remove(s[l])
                l += 1
            res = max(res, r-l+1)
            collection.add(s[r])
        return res
