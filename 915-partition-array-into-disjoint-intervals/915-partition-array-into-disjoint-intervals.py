class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        L = len(nums)
        left_max, right_min = [0]*L, [0]*L
        left_max[0], right_min[L-1] = nums[0], nums[L-1]
        sol_idx = 0
        for i in range(L-2, -1, -1):
            right_min[i] = min(right_min[i+1], nums[i])
            
        for i in range(1, L):
            left_max[i] = max(left_max[i-1], nums[i])
            if right_min[i] >= left_max[i-1]:
                return i
        return -1
        