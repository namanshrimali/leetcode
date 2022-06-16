class Solution:
    def minSwaps(self, data: List[int]) -> int:
        window_size = sum(data) # total ones is the window size
        total_swaps_required = zeros_in_window = window_size - sum(data[:window_size])
        
        for i in range(1, len(data) - window_size + 1):
            if data[i-1] == 0:
                zeros_in_window -= 1
            if data[i + window_size - 1] == 0:
                zeros_in_window += 1
            total_swaps_required = min(total_swaps_required, zeros_in_window)
        return total_swaps_required
