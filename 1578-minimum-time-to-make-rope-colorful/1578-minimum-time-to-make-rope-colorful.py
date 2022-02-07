class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        time, L = 0, len(colors)
        def remove_same_baloons(idx, color):
            total_time = max_time = 0
            
            while idx < L and colors[idx]==color:
                total_time+=neededTime[idx]
                max_time = max(max_time, neededTime[idx])
                idx+=1
            return total_time - max_time, idx
        idx = 0
        while idx < L:
            min_time, idx = remove_same_baloons(idx, colors[idx])
            time+=min_time
            
        return time