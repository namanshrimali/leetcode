class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        L = len(nums)
        right_min = [0]*L
        right_min[L-1] = nums[L-1]
        
        for i in range(L-2, -1, -1):
            right_min[i] = min(right_min[i+1], nums[i])
        
        curr_left_max = nums[0]
        for i in range(1, L):
            if right_min[i] >= curr_left_max:
                return i
            curr_left_max = max(curr_left_max, nums[i])
        return -1
        