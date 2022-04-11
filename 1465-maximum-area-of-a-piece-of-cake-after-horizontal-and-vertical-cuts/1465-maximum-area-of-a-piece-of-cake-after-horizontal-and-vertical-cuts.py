class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        MOD = 10**9+7
        horizontalCuts.sort(), verticalCuts.sort()
        
        max_height, max_width = -inf, -inf
        
        horizontalCuts = [0] + horizontalCuts + [h]
        verticalCuts = [0] + verticalCuts + [w]
        
        for i in range(1, len(horizontalCuts)):
            local_max = horizontalCuts[i] - horizontalCuts[i-1]
            max_height = max(max_height, local_max)
        
        for i in range(1, len(verticalCuts)):
            local_max = verticalCuts[i]-verticalCuts[i-1]
            max_width = max(max_width, local_max)
        
        return (max_width * max_height)%MOD
            
        