class Solution:
    def frequencySort(self, s: str) -> str:
        if not s or len(s) == 1:
            return s
        char_freq_counter = {}
        max_freq = 0
        for char in s:
            char_freq_counter[char] = char_freq_counter.get(char, 0) + 1
            max_freq = max(max_freq, char_freq_counter[char])
        buckets = [[] for _ in range(max_freq)]
        
        for char in char_freq_counter:
            freq = char_freq_counter[char]
            buckets[freq - 1].append(char)
        frequency_sorted_array = []
        for i in range(len(buckets) - 1, -1, -1):
            for char in buckets[i]:
                frequency_sorted_array.append(char * (i + 1))
        return ''.join(frequency_sorted_array)
        