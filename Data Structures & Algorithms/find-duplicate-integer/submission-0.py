class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Naive solution
        seen = set()
        for n in nums:
            if n in seen:
                return n
            else:
                seen.add(n)
        return -1