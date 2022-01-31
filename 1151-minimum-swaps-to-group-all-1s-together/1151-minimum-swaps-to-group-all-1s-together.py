class Solution:
    def minSwaps(self, data: List[int]) -> int:
        L = len(data)
        total_ones = 0
        for i in range(L):
            if data[i] == 1:
                total_ones+=1 
                
        left, right = 0, 0
        max_ones, ones_in_window = 0, 0
        while right<L:
            if right-left+1 > total_ones:
                if data[left] == 1:
                    ones_in_window -=1
                left+=1
            if data[right] == 1:
                ones_in_window+=1
            max_ones = max(max_ones, ones_in_window)
            right+=1
        return total_ones - max_ones
        