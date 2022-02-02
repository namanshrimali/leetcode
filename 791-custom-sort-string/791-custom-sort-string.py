class Solution:
    def customSortString(self, order: str, s: str) -> str:
        hash_map = {}
        for i in range(len(order)):
            hash_map[order[i]] = i+1
        s = list(s)
        s.sort(key= lambda a:hash_map.get(a, 27))
        return ''.join(s)