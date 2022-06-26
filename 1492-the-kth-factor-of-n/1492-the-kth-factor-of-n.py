class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        sqrt_n = int(n**(0.5))
        is_perfect_square = sqrt_n ** 2 == n
        factors = []
        factor_len = 0
        for i in range(1, sqrt_n+1):
            if n%i == 0:
                factors.append(i)
                k -= 1
                factor_len += 1
            if k == 0:
                return factors[-1]
        if is_perfect_square:
            k+=1
        return n//factors[factor_len - k] if k <= factor_len else -1
