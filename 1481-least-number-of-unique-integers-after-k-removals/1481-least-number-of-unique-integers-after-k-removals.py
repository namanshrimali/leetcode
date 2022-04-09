class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = {}
        for num in arr:
            counter[num] = counter.get(num, 0)+1
        min_heap = []
        for num in counter:
            heapq.heappush(min_heap, [counter[num], num])
    
        while k:
            freq, top_ele = heapq.heappop(min_heap)
            freq -=1
            if freq:
                heapq.heappush(min_heap, [freq, top_ele])
            else:
                del counter[top_ele]
            k-=1
        return len(counter)