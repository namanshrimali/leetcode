class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)
        last, total_negatives = 0, 0
        non_zero_subarrays = []
        
        for curr, num in enumerate(nums):
            if num == 0:
                non_zero_subarrays.append([nums[last:curr], total_negatives])
                total_negatives = 0
                last = curr + 1
            if num < 0:
                total_negatives += 1
        
        if last < n:
            non_zero_subarrays.append([nums[last:], total_negatives])
        
        max_positive_subarray_len = 0
        
        for subarray, subarray_negatives in non_zero_subarrays:
            if subarray_negatives % 2 == 0:
                max_positive_subarray_len = max(max_positive_subarray_len, len(subarray))
            else:
                max_sub_subarray_len = 0
                l = len(subarray)
                for i in range(l):
                    if subarray[i] < 0:
                        max_sub_subarray_len = max(i, l - i - 1)
                        max_positive_subarray_len  = max(max_positive_subarray_len, max_sub_subarray_len)
        return max_positive_subarray_len