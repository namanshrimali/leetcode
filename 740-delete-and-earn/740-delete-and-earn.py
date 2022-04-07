class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points_map = {}
        for num in nums:
            points_map[num] = points_map.get(num, 0) + num
        sorted_keys = sorted(points_map.keys())
        
        last_key = sorted_keys[0]
        
        prev_max, second_prev_max = points_map[last_key], 0
        
        for curr_key in sorted_keys[1:]:
            if curr_key == last_key+1:
                curr_max = max(second_prev_max+ points_map[curr_key], prev_max)
            else:
                curr_max = prev_max + points_map[curr_key]
            last_key = curr_key
            second_prev_max = prev_max
            prev_max = curr_max
        return prev_max
