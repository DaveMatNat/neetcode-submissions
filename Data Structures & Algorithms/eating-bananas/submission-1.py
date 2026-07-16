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
                upper = k - 1
            else: # total_hours > k
                lower = k + 1
        return min_k


            
