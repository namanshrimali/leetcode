class Solution:
    def sumZero(self, n: int) -> List[int]:
        half_len = n//2
        sol = [0]*n
        for i in range(n):
            sol[i] = 2*i-n+1
        return sol