class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Better solution

        nums.sort() # O(nlogn)
        length = len(nums)
        res = []

        for i1 in range(length):
            if nums[i1] > 0:
                break # impossible to get the nums to add up to zero
            
            if i1 > 0 and nums[i1] == nums[i1-1]:
                continue # duplicate starting point

            i2, i3 = i1+1, length-1
            while i2 < i3:
                if nums[i1] + nums[i2] + nums[i3] == 0:
                    res.append([nums[i1],nums[i2],nums[i3]])
                    i2 += 1
                    i3 -= 1
                    # in case the starting point i2 is still the same
                    while nums[i2] == nums[i2-1] and i2 < i3:
                        i2 += 1
                elif nums[i1] + nums[i2] + nums[i3] > 0:
                    i3 -= 1
                else:
                    i2 += 1
        
        return res
