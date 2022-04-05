class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 1
        intervals.sort(key= lambda a: a[0])
        free_rooms = [] # maintaining min heap of rooms with earliest end time  
        heapq.heappush(free_rooms, intervals[0][1])
        
        for start, end in intervals[1:]:
            if free_rooms[0] <= start:
                heapq.heappop(free_rooms)
            heapq.heappush(free_rooms, end)
        return len(free_rooms)

        
        