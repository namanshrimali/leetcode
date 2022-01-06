class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        hash_map = {}
        for string in strings:
            string_token = ""
            for i in range(1, len(string)):
                string_token += str((ord(string[i-1]) - ord(string[i]))%26)
            if string_token in hash_map:
                hash_map[string_token].append(string)
            else:
                hash_map[string_token] = [string]
                
        return list(hash_map.values())