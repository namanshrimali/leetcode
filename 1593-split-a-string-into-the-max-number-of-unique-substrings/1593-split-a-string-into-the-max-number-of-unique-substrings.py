class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        sol = 0
        L = len(s)
        def backtrack(idx, sub_s = []):
            nonlocal sol
            if idx == L:
                sol = max(sol, len(sub_s))
                return
            for i in range(idx+1, L+1):
                part = s[idx:i]
                if part not in sub_s:
                    backtrack(i, sub_s+[part])
        backtrack(0)
        return sol
        