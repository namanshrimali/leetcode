class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        sqrt_n = int(n**0.5)
        is_perfect_square = sqrt_n * sqrt_n == n
        factors = []
        for i in range(1, sqrt_n+1):
            if n%i == 0:
                factors.append(i)
                k-=1
            if k == 0:
                return i
        if is_perfect_square:
            k+=1
        
        if k > len(factors):
            return -1
        
        else:
            return n//(factors[len(factors)-k])
        