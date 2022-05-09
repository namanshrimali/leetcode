class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        total_cost = 0
        while len(sticks) > 1:
            stick_a = heapq.heappop(sticks)
            stick_b = heapq.heappop(sticks)
            new_stick = stick_a + stick_b
            total_cost += new_stick
            heapq.heappush(sticks, new_stick)
        return total_cost