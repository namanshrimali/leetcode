class MedianFinder:

    def __init__(self):
        self.max_heap, self.min_heap = [], []
    
    def _min_to_max(self):  # right list to left list
        next_max = heapq.heappop(self.min_heap)
        heapq.heappush(self.max_heap, -next_max)
        
    def _max_to_min(self):  # left list to right list
        next_smallest = - heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap, next_smallest)
        

    def addNum(self, num: int) -> None:
        if self.max_heap:
            if num <= -self.max_heap[0]:
                heapq.heappush(self.max_heap, -num)
            else:
                heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, -num)
        
        if len(self.max_heap) > len(self.min_heap)+1:
            self._max_to_min()
        elif len(self.min_heap) > len(self.max_heap)+1:
            self._min_to_max()
        

    def findMedian(self) -> float:
        if len(self.max_heap)> len(self.min_heap):
            return -self.max_heap[0]
        elif len(self.min_heap)> len(self.max_heap):
            return self.min_heap[0]
        else:
            return (self.min_heap[0]-self.max_heap[0])/2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()