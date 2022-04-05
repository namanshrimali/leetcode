class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        heap = []
        for qnty, units in boxTypes:
            heapq.heappush(heap, [-units, qnty])
        total_units = 0
        
        while heap and truckSize:
            units, qnty = -heap[0][0], heap[0][1]
            req = min(qnty, truckSize)
            qnty -= req
            truckSize -= req
            total_units += req * units 
            
            if qnty == 0:
                heapq.heappop(heap)
                
        return total_units