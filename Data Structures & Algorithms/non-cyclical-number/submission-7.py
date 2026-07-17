class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        num = n
        while num != 1:
            if num in seen:
                print(num, seen)
                return False
            seen.add(num)
            size = len(str(num))-1
            add = 0
            while (size >= 0):
                digit = num // (10**size)
                add += (digit)**2
                num -= digit * (10**size)
                size -= 1
            num = add
        return True