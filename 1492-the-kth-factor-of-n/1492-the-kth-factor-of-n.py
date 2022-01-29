class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        heap = []
        stop = int(n**0.5)
        
        def heappush_k(num):
            heapq.heappush(heap, -num)
            if len(heap) > k:
                heapq.heappop(heap)
                
        for num in range(1, stop+1):
            if n%num==0:
                heappush_k(num)
                if n//num != num:
                    heappush_k(n//num)
        return -heapq.heappop(heap) if len(heap) == k else -1