class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for n in s:
            # n is the beginning of a sequence <=> n-1 is not in set(nums)
            if (n - 1) not in nums:
                # start with length 1
                length = 1
                # if consecutive number incrementally exist increase length
                while (n+length) in s:
                    length += 1
                # take the max of current vs the latest consecutive length
                res = max(length, res)
        return res
        