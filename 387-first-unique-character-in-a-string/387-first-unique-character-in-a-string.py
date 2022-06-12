class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_counter = {}
        for char in s:
            char_counter[char]  = char_counter.get(char, 0) + 1
        for i, char in enumerate(s):
            if char_counter[char] == 1:
                return i
        return -1
            