class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window_char_map = {}
        left = 0
        max_window_size = 0
        
        for right, char in enumerate(s):
            if char in window_char_map and window_char_map[char] != '-1':
                for j in range(left, window_char_map[char]+1):
                    left = j+1
                    window_char_map[s[j]] = -1
            max_window_size = max(right - left + 1, max_window_size)
            window_char_map[char] = right
            
        return max_window_size