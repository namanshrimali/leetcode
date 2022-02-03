class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance_from_origin(point):
            x, y = point[0], point[1]
            return math.sqrt(x**2 + y**2)
        heap = []
        for point in points:
            heapq.heappush(heap, (-distance_from_origin(point), point[0], point[1]))
            if len(heap) > k:
                heapq.heappop(heap)
        return [[x, y] for dist, x, y in heap]
        
                
                
        