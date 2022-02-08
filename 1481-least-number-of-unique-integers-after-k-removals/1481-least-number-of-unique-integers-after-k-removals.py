class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter_map = {}
        for num in arr:
            counter_map[num] = counter_map.get(num, 0)+1
        heap = []
        for key in counter_map:
            heapq.heappush(heap, counter_map[key])
        while k:
            lowest_freq = heapq.heappop(heap)
            if lowest_freq > k:
                heapq.heappush(heap, lowest_freq-k)
                k = 0
                continue
            k-= lowest_freq
        return len(heap)
            