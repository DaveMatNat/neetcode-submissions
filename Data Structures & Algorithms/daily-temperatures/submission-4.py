class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures) 
        stack = [] # pair : [temp, index]

        # Stack is going to be in monotonically decreasing order
        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]: # if the new temp > top of the stack
                stackT, stackIdx = stack.pop() # pop the top
                diff = i - stackIdx # how many days
                res[stackIdx] = diff # for the top of the stack, the gap with new temp is diff days
            
            # add this new temp to the stack (which is monotonically decreasing)
            stack.append([t,i]) 
        return res