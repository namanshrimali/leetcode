class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 1:
            return x
        if n == 0:
            return 1
        if n < 0:
            x = 1/x
            n = -n
        half_pow = self.myPow(x, n//2)
        sol = half_pow**2
        if n%2!=0:
            sol = sol*x
        return sol