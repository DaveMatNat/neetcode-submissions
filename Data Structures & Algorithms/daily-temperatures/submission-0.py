class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        res = [0] * length

        for l in range(length):
            curr_temp = temperatures[l]
            for r in range(l+1, length):
                next_temp = temperatures[r]
                if next_temp > curr_temp:
                    res[l] = r-l
                    break
        return res

