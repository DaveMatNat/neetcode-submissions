class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for n in s:
            if (n - 1) not in nums:
                length = 1
                while (n+length) in s:
                    length += 1
                res = max(length, res)
        return res
        