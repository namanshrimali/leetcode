class Solution:
    def trap(self, height: List[int]) -> int:
        L = len(height)
        left_max, right_max = [0]*L, [0]*L
        left_max[0], right_max[L-1] = height[0], height[L-1]
        for i in range(1, L):
            left_max[i] = max(left_max[i-1], height[i])
        for i in range(L-2, -1, -1):
            right_max[i] = max(height[i], right_max[i+1])
        sol = 0
        for i in range(1, L):
            sol+=min(left_max[i], right_max[i])-height[i]
        return sol
        