class Solution:
    def climbStairs(self, n: int) -> int:

        if n < 2:
            return n
        # you only really need the last two values
        last_1, last_2 = 1,2 # initialize to the first two base cases

        for s in range(3, n+1):
            temp = last_2
            last_2 = temp + last_1
            last_1 = temp
        return last_2