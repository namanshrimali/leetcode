class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heap = []
        for stick in sticks:
            heapq.heappush(heap, stick)
        total_cost = 0
        while len(heap)>1:
            first, second = heapq.heappop(heap), heapq.heappop(heap)
            final_stick = first+second
            total_cost += final_stick
            heapq.heappush(heap, final_stick)
        return total_cost
            