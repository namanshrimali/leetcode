class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set([0])
        room_queue = collections.deque([0])
        while room_queue:
            curr_room = room_queue.popleft()
            for next_room in rooms[curr_room]:
                if next_room not in visited:
                    room_queue.append(next_room)
                    visited.add(next_room)
        return len(visited) == len(rooms)
        