class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        event_heap = []
        max_days = 0
        for start, end in events:
            max_days = max(max_days, end)
            heapq.heappush(event_heap, [start, end])
        event_priority = []

        curr_day, total_events_attended = 0, 0
        
        while curr_day <= max_days:
            curr_day += 1
            while event_priority and event_priority[0] < curr_day:
                heapq.heappop(event_priority)
                
            while event_heap and event_heap[0][0] == curr_day:
                heapq.heappush(event_priority, heapq.heappop(event_heap)[1])
            
            if event_priority:
                heapq.heappop(event_priority)
                total_events_attended += 1

        return total_events_attended
                