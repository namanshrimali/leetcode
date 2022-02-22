class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev, curr = 0, 1
        sol = 0
        for i in range(1, len(s)):
            if s[i-1] != s[i]:
                # change in letter, 0->1 or 1->0
                sol += min(prev, curr)
                prev = curr
                curr = 1
            else:
                curr += 1
        sol += min(prev, curr)
        return sol