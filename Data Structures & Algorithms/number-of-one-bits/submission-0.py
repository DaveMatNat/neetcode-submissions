class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for shift in range(32):
            if (1 << shift & n) == (1 << shift):
                count += 1
        return count