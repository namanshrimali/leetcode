class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        time, L = 0, len(colors)
        def remove_same_baloons(idx, color):
            min_time = 0
            min_heap = []
            while idx < L and colors[idx]==color:
                heapq.heappush(min_heap, neededTime[idx])
                idx+=1
            while len(min_heap)>1:
                min_time+=heapq.heappop(min_heap)
            return min_time, idx
        idx = 0
        while idx < L:
            min_time, idx = remove_same_baloons(idx, colors[idx])
            time+=min_time
        return time