class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda interval : interval[0])
        heap = []
        
        for start, end in intervals:
            
            if heap and heap[0] <= start:
                heapq.heappop(heap)
            heapq.heappush(heap, end)
            
        return len(heap)
