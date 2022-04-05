class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        last, curr, no_of_negatives = 0, 0, 0
        non_zero_subarrays = []
        for i in range(len(nums)):
            if nums[i] == 0:
                non_zero_subarrays.append((nums[last:curr], no_of_negatives))
                last = curr+1
                no_of_negatives = 0
            if nums[i] < 0:
                no_of_negatives +=1
            curr+=1
        if last < len(nums):
            non_zero_subarrays.append((nums[last:], no_of_negatives))
        
        max_len = 0
        for array, no_negatives in non_zero_subarrays:
            array_len = len(array)
            if no_negatives % 2 == 0:
                if array_len > max_len:
                    max_len = array_len
            else:
                for i in range(array_len):
                    if array[i] < 0:
                        sub_arr_max = max(i, array_len-i-1)
                        max_len = max(max_len, sub_arr_max)
                    
        return max_len