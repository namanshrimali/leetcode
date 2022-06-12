class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_counter = [0] * 26
        def get_idx(char):
            return ord(char) - ord('a')
        for char in s:
            idx = get_idx(char)
            char_counter[idx]  += 1
        for i, char in enumerate(s):
            idx = get_idx(char)
            if char_counter[idx] == 1:
                return i
        return -1
            