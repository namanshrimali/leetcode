class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        L = len(s)
        prefix = [0]*(L+1)
        for i in range(L):
            prefix[i+1] = prefix[i]+int(s[i])
        sol = float('inf')
        for i in range(L+1):
            ones_till_i, ones_after_i = prefix[i], prefix[L]-prefix[i]
            zeros_after_i = L-i-ones_after_i
            # need to flip ones before i and zeros after i to make string monotonically increasing, min is kept in sol
            sol = min(sol, ones_till_i+zeros_after_i)
        return sol
            