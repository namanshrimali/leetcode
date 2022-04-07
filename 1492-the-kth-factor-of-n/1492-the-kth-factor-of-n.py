class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        divisors = []
        sqrt_n = int(n**0.5)
        for i in range(1, sqrt_n+1):
            if n%i == 0:
                divisors.append(i)
                k-=1
                if k == 0:
                    return i
        
        if (sqrt_n*sqrt_n == n):
            k+=1
            
        if k > len(divisors):
            return -1
        else:
            return n//divisors[len(divisors)-k]