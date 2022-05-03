class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        left_ones = [0] * (n+1)
        total_ones = 0
        for i in range(n):
            if s[i] == '1':
                left_ones[i+1] = left_ones[i] + 1
                total_ones += 1
            else:
                left_ones[i+1] = left_ones[i]
        two_way_flips = inf
        right_zeros = 0
        for i in range(n-1, -1, -1):
            if s[i] == '0':
                right_zeros += 1
            two_way_flips = min(two_way_flips, right_zeros + left_ones[i])
        
        return min(total_ones, n-total_ones, two_way_flips)        