class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        min_heap = []
        counter = {}
        for num in arr:
            counter[num] = counter.get(num, 0) + 1
        
        for num in counter:
            heapq.heappush(min_heap, [counter[num], num])
        
        while k>0 and min_heap:
            count, element = min_heap[0]
            k -= count  
            if k >= 0:
                heapq.heappop(min_heap)

        return len(min_heap)
