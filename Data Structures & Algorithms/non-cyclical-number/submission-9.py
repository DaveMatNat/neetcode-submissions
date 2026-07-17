class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        num = n
        while num != 1:
            if num in seen:
                return False
            seen.add(num)
            size = len(str(num))-1
            add = sum(int(d)**2 for d in str(num))
            num = add
        return True