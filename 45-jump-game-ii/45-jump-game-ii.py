class Solution:
    def jump(self, nums: List[int]) -> int:
        farthest, curr_jump_idx, total_jumps = 0, 0, 0
        
        for i in range(len(nums)-1):
            farthest = max(farthest, i+nums[i])
            if curr_jump_idx == i:
                curr_jump_idx = farthest
                total_jumps +=1
        return total_jumps
            
        