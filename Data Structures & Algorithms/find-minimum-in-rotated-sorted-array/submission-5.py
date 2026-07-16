class Solution:
    def findMin(self, nums: List[int]) -> int:
        def search(left: int, right: int) -> int:

            # If this portion is already sorted,

            # the leftmost element is the minimum.

            if nums[left] <= nums[right]:

                return nums[left]

            mid = (left + right) // 2

            # Left half is sorted, so the minimum must be in the right half.

            if nums[mid] >= nums[left]:

                return search(mid + 1, right)

            # Otherwise the rotation point is in the left half.

            else:

                return search(left, mid)

        return search(0, len(nums) - 1)