class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Better solution

        nums.sort() # O(nlogn)
        length = len(nums)
        res = set()

        for i1 in range(length):
            i2, i3 = i1+1, length-1
            while i2 < i3:
                if nums[i1] + nums[i2] + nums[i3] == 0:
                    res.add(tuple([nums[i1],nums[i2],nums[i3]]))
                    i2 += 1
                    i3 -= 1
                elif nums[i1] + nums[i2] + nums[i3] > 0:
                    i3 -= 1
                else:
                    i2 += 1
        
        return [list(l) for l in res]
