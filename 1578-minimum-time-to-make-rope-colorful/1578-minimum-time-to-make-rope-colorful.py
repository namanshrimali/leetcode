class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        def remove_adj_colours(idx, colour):
            total_time, max_time = 0, 0
            while idx < len(colors) and colors[idx] == colour:
                total_time += neededTime[idx]
                if neededTime[idx] > max_time:
                    max_time = neededTime[idx]
                idx+=1
            return total_time - max_time, idx-1
        total_time, i = 0, 0
        while i < len(colors):
            time_taken, i = remove_adj_colours(i, colors[i])
            total_time += time_taken
            i+=1
        return total_time
        
            