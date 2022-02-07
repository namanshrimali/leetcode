class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_arr = [0]*26
        for letter in s:
            char_arr[ord(letter)-ord('a')]+=1
        for idx, letter in enumerate(s):
            if char_arr[ord(letter)-ord('a')]==1:
                return idx
        return -1        