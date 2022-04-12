class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + num
            
        sorted_nums = sorted(counter.keys())
        prev_max, second_prev_max = counter[sorted_nums[0]], 0
        
        for i in range(1, len(sorted_nums)):
            if sorted_nums[i-1] < sorted_nums[i]-1:
                curr_max = prev_max + counter[sorted_nums[i]]
            else:
                curr_max = max(prev_max, counter[sorted_nums[i]] + second_prev_max)
            second_prev_max = prev_max
            prev_max = curr_max
        
        return prev_max