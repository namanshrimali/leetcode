class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        L = len(nums)
        right_min = [0] * L
        right_min[-1] = nums[-1]
        for i in range(L-2, -1, -1):
            right_min[i] = min(right_min[i+1], nums[i])
        left_max = nums[0]
        for i in range(1, L):
            if left_max <= right_min[i]:
                break
            left_max = max(left_max, nums[i])
        return i
            
            
        