class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        heap = []
        for qnty, units in boxTypes:
            heapq.heappush(heap, [-units, qnty])
        
        total_units = 0
        
        while truckSize and heap:
            units_per_box, qnty = -heap[0][0], heap[0][1]
            
            while qnty and truckSize:
                total_units += units_per_box
                truckSize -=1
                qnty-=1
                
            if qnty == 0:
                heapq.heappop(heap)
        
        return total_units