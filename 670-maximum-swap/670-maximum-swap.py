class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))
        left, right = 0, 0
        right_max_idx = len(num)-1
        for i in range(len(num)-2, -1, -1):
            if num[i] > num[right_max_idx]:
                right_max_idx = i
            elif num[i] < num[right_max_idx]:
                left = i
                right = right_max_idx
        num[left], num[right] = num[right], num[left]
        return int(''.join(num))
                