class Solution:
    def minSwaps(self, data: List[int]) -> int:
        window_size = 0
        
        for num in data:
            window_size += num
        
        zeros_in_window = 0
        
        for i in range(window_size):
            if data[i] == 0:
                zeros_in_window += 1
        min_swaps = zeros_in_window  

        for i in range(1, len(data) - window_size + 1):
            if data[i-1] == 0:
                zeros_in_window -= 1
            if data[i+window_size - 1] == 0:
                zeros_in_window += 1

            min_swaps = min(min_swaps, zeros_in_window)
        return min_swaps
