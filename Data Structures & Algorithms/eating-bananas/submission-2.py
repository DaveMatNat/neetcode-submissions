class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Second approach
        
        # O(n) to find max
        lower, upper = 1, max(piles)
        min_k = upper

        while lower <= upper: # O(log(m))
            k = (lower+upper)//2
            total_hours = 0
            for p in piles: #O(n)
                hours = math.ceil(p/k)
                total_hours += hours
            if total_hours <= h:
                min_k = min(min_k, k)
                upper = k - 1 # We know for sure that k gets you under h, but is there a lower k? Thus we reduce the upper bound
            else: # total_hours > h
                lower = k + 1 # k (mid) took too much time, so the k must be at a higher rate than that
        return min_k


            
