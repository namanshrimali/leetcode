class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)
        max_pos_subarray_len = 0
        non_zero_subarrays = []
        total_negatives = 0
        prev = 0
        for curr in range(n):
            if nums[curr] == 0:
                non_zero_subarrays.append([nums[prev:curr], total_negatives])
                total_negatives = 0
                prev = curr + 1
            if nums[curr] < 0:
                total_negatives += 1
        
        if prev < n:
            non_zero_subarrays.append([nums[prev:], total_negatives])
        
        for non_zero_subarray, total_negatives in non_zero_subarrays:
            if total_negatives % 2 == 0:
                max_pos_subarray_len = max(max_pos_subarray_len, len(non_zero_subarray))
            else:
                l = len(non_zero_subarray)
                for i in range(l):
                    if non_zero_subarray[i] < 0:
                        max_sub_subarray_len = max(i, l - i - 1)
                        max_pos_subarray_len = max(max_pos_subarray_len, max_sub_subarray_len)
        return max_pos_subarray_len
    