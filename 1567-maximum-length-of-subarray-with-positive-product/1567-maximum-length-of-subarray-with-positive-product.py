class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)
        pos_arr, neg_arr = [0]*n, [0]*n
        if nums[0] > 0: 
            pos_arr[0] = 1
        if nums[0] < 0:
            neg_arr[0] = 1
            
        for i in range(1, n):
            num = nums[i]
            if num > 0:
                pos_arr[i] = pos_arr[i-1] + 1
                neg_arr[i] = neg_arr[i-1] + 1 if neg_arr[i-1] > 0 else 0
    
            elif num < 0:
                pos_arr[i] = neg_arr[i-1] + 1 if neg_arr[i-1] > 0 else 0
                neg_arr[i] = pos_arr[i-1] + 1
        return max(pos_arr)
                