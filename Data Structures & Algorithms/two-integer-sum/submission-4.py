class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = {}
        for i, val in enumerate(nums):
            diff = target - val
            if diff in complement:
                return [complement[diff], i]
            complement[val] = i
        return [-1,-1]