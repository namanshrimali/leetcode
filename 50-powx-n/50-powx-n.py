class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n ==0:
            return 1
        if n < 0:
            x = 1/x
            n = -n
        if n == 1:
            return x
        product = 1
        half_product = self.myPow(x, n//2)
        product = half_product * half_product
        if n%2==1:
            product*= x
        return product