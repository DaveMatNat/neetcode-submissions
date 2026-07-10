class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count_zeroes = 0
        prod = 1
        res = [0]*len(nums)
        for n in nums:
            if n == 0:
                count_zeroes += 1
            else:
                prod *= n
        
        if count_zeroes >= 2:
            return res
        elif count_zeroes == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    res[i] = prod
                    return res
        else:   
            for i in range(len(nums)):
                res[i] = prod // nums[i]
            return res