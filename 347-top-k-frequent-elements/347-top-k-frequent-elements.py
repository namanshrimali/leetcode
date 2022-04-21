class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        heap = []
        for num in counter:
            heapq.heappush(heap, [counter[num], num])
            if len(heap) > k:
                heapq.heappop(heap)
        for i in range(k):
            heap[i] = heap[i][1]
        return heap