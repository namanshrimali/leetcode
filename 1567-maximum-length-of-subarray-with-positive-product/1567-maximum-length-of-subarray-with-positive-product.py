class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        last, curr, no_of_negatives = 0, 0, 0
        non_zero_subarrays = []
        for i, num in enumerate(nums):
            if num == 0:
                non_zero_subarrays.append((nums[last:curr], no_of_negatives))
                last = curr + 1
                no_of_negatives = 0
            if num < 0:
                no_of_negatives += 1
            curr += 1    
        
        if last < len(nums):
            non_zero_subarrays.append((nums[last:], no_of_negatives))
        max_pos_subarr = 0
        
        for arr, no_of_negatives in non_zero_subarrays:
            if no_of_negatives % 2 == 0:
                max_pos_subarr = max(max_pos_subarr, len(arr))
            else:
                local_max = 0
                for i in range(len(arr)):
                    if arr[i] < 0:
                        local_max = max(i, len(arr)-i-1)
                        max_pos_subarr = max(max_pos_subarr, local_max)
        return max_pos_subarr