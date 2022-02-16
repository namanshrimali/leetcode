class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        count_map = {}
        for num in nums:
            count_map[num] = count_map.get(num, 0)+1
        for num in count_map:
            heapq.heappush(heap, (count_map[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [x for _, x in heap]
        