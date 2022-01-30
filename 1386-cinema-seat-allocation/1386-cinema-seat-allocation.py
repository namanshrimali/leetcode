class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        acceptable_groups = [[2,3,4,5], [4,5,6,7], [6,7,8,9]]
        seat_map = {}
        for row, seat in reservedSeats:
            blocked_groups = set()
            for i in range(3):
                if seat in acceptable_groups[i]:
                    blocked_groups.add(i)
            if blocked_groups:
                seat_map[row] = seat_map.get(row, set()).union(blocked_groups)
        
        total_groups = 2*n
        for row in seat_map:
            if len(seat_map[row]) == 3:
                total_groups-=2
            else:
                total_groups-=1
                
        return total_groups