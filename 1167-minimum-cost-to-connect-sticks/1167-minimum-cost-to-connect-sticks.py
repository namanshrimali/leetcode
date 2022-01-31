class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        total = 0
        while len(sticks)>=2:
            smallest, second_smallest = heapq.heappop(sticks), heapq.heappop(sticks)
            bigger_stick = smallest+second_smallest
            total+= bigger_stick
            heapq.heappush(sticks, bigger_stick)
        return total
        