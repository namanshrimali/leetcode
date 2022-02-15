class Solution:
    def maximumSwap(self, num: int) -> int:
        # if number is highest on the right, no swapping of that number
        # if number is not highest, swap it with highest number on the right
        num = list(str(num))
        L = len(num)
        left, right = 0, 0
        right_max_idx = L-1
        for i in range(L-2, -1, -1):
            if num[i] > num[right_max_idx]:
                right_max_idx = i
            elif num[i] < num[right_max_idx]:
                left = i
                right = right_max_idx
        num[left], num[right] = num[right], num[left]    
        return ''.join(num)