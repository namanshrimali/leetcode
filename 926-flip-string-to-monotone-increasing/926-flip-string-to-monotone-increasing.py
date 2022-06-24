class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        s = list(s)
        n = len(s)
        ones_on_left = [0] * (n)
        total_ones = 1 if s[0] == '1' else 0 
        
        for i in range(1, n):
            if s[i-1] == '1':
                ones_on_left[i] = ones_on_left[i-1] + 1
            else:
                ones_on_left[i] = ones_on_left[i-1]
            if s[i] == '1':
                total_ones += 1
        
        zeroes_on_right = [0] * (n+1)
        
        for i in range(n-1, -1, -1):
            if s[i] == '0':
                zeroes_on_right[i] = zeroes_on_right[i+1] + 1
            else:
                zeroes_on_right[i] = zeroes_on_right[i+1]
        
        minimal_zero_one_flips = min(total_ones, n-total_ones)

        for i in range(n):
            minimal_zero_one_flips = min(minimal_zero_one_flips, ones_on_left[i] + zeroes_on_right[i])
        return minimal_zero_one_flips
            
        