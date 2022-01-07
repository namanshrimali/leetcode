class Solution:
    def customSortString(self, order: str, s: str) -> str:
        hash_map = {}
        for char in s:
            hash_map[char] = hash_map.get(char, 0)+1
        ans = []
        for o in order:
            ans.append(o*hash_map.get(o, 0))
            hash_map[o] = 0
        for char in hash_map:
            ans.append(char*hash_map[char])
        return ''.join(ans)