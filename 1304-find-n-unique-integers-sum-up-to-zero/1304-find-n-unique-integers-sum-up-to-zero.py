class Solution:
    def sumZero(self, n: int) -> List[int]:
        half_len = n//2
        sol = []
        for i in range(1, half_len+1):
            sol.append(-i)
            sol.append(i)
        if n-2*half_len == 1:
            sol.append(0)
        return sol