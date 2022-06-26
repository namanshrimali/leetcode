class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        num_counter = {}
        for num in nums:
            num_counter[num] = num_counter.get(num, 0) + num
            
        sorted_nums = list(sorted(num_counter.keys()))
        
        second_last_max_points, last_max_points = 0, num_counter[sorted_nums[0]]
        
        for i in range(1, len(sorted_nums)):
            curr_num_points = num_counter[sorted_nums[i]]
            if sorted_nums[i-1] == sorted_nums[i]-1:
                curr_max = max(curr_num_points + second_last_max_points, last_max_points)
            else:
                curr_max = curr_num_points + last_max_points
            second_last_max_points = last_max_points
            last_max_points = curr_max
        
        return last_max_points