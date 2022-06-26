class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        sqrt_n = int(n**(0.5))
        is_perfect_square = sqrt_n ** 2 == n
        factors = []
        for i in range(1, sqrt_n+1):
            if n%i == 0:
                factors.append(i)
                k -= 1
            if k == 0:
                return factors[-1]
        if is_perfect_square:
            k+=1
        
        return n//factors[len(factors) - k] if k <= len(factors) else -1
