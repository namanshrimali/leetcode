class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev, curr = [], []
        sol = 0
        for i in range(len(s)):
            if i > 0 and s[i-1] != s[i]:
                # change in letter, 0->1 or 1->0
                sol += min(len(prev), len(curr))
                prev = curr
                curr = [s[i]]
            else:
                curr.append(s[i])
        sol += min(len(prev), len(curr))
        return sol