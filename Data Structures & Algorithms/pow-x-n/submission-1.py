class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n > 0:
            if n % 2 == 0:
                temp = self.myPow(x, n/2)
                return temp * temp
            else:
                temp = self.myPow(x, (n-1)/2)
                return x * temp * temp
        else:
            # if n % 2 == 0:
            #     temp = myPow(x, -n/2)
            #     return 1/temp * 1/temp
            # else:
            #     return x * myPow(x, (n-1)/2) * myPow(x, (n-1)/2)
            return 1/self.myPow(x,-n)