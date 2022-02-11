class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        MOD = 1_000_000_000+7
        
        horizontalCuts.sort(), verticalCuts.sort()
        
        horizontalCuts = [0] + horizontalCuts + [h]
        verticalCuts = [0] + verticalCuts + [w]
        
        max_hor, max_ver = -inf, -inf
        
        for i in range(1, len(horizontalCuts)):
            max_hor = max(max_hor, horizontalCuts[i] - horizontalCuts[i-1])
        
        for i in range(1, len(verticalCuts)):
            max_ver = max(max_ver, verticalCuts[i] - verticalCuts[i-1])
            
        return (max_hor*max_ver)%MOD
        
        