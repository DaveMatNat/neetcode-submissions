class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        running_front = [1] * len(nums)
        running_back = [1] * len(nums)
        res = [1] * len(nums)

        # front
        for i in range(1, len(nums)):
            running_front[i] = running_front[i-1] * nums[i-1]
        print(running_front)

        # back
        for j in range(len(nums)-2,-1, -1):
            running_back[j] = running_back[j+1] * nums[j+1]
        print(running_back)

        for i in range(len(running_front)):
            res[i] = running_back[i] * running_front[i]
            
        return res