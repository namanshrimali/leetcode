class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        hash_map = {}
        for string in strings:
            diff = []
            for i in range(1, len(string)):
                diff.append((ord(string[i])-ord(string[i-1]))%26)
            diff = ''.join(str(diff))
            if diff in hash_map:
                hash_map[diff].append(string)
            else:
                hash_map[diff] = [string]
        return list(hash_map.values())