class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = {}
        # nums[i] == target - nums[j]
        for i, val in enumerate(nums):
            comp = target - val
            if comp in complement:
                return [complement[comp], i]
            complement[val] = i
        return [-1,-1]