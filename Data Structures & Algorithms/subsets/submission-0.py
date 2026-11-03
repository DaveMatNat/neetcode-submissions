class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]

        first = nums[0]
        rest = self.subsets(nums[1:])

        exclude = rest
        include = [[first] + subset for subset in rest]

        return exclude + include
