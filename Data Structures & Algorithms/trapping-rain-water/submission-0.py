class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        for i in range(len(height)):
            leftMax = height[i]
            rightMax = height[i]

            for j in range(i):
                leftMax = max(leftMax, height[j])
            for j in range(i+1, len(height)):
                rightMax = max(rightMax, height[j])
            
            total += min(leftMax, rightMax) - height[i]
        return total