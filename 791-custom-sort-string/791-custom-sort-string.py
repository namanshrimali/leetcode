class Solution:
    def customSortString(self, order: str, s: str) -> str:
        hash_map = {}
        for i in range(len(s)):
            hash_map[s[i]] = hash_map.get(s[i], 0)+1
        sol = []
        for char in order:
            if char in hash_map:
                sol.append(char*hash_map[char])
                del hash_map[char]
        for remaining in hash_map:
            sol.append(remaining*hash_map[remaining])
        return ''.join(sol)