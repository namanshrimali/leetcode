class Solution:
    def maximumSwap(self, num: int) -> int:
        # if number is highest on the right, no swapping of that number
        # if number is not highest, swap it with highest number on the right
        num = list(str(num))
        L = len(num)
        max_arr = [0] * L
        max_arr[L-1] = L-1
        for i in range(L-2, -1, -1):
            if num[i] > num[max_arr[i+1]]:
                max_arr[i] = i
            else:
                max_arr[i] = max_arr[i+1]
        for i in range(len(num)):
            if num[i] < num[max_arr[i]]:
                num[i], num[max_arr[i]]  = num[max_arr[i]], num[i]
                break
        return ''.join(num)