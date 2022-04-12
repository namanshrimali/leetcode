class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        max_heap = []
        for qnty, units_per_box in boxTypes:
            heapq.heappush(max_heap, [-units_per_box, qnty])
        max_units = 0
        
        while max_heap and truckSize:
            units_per_box, qnty = heapq.heappop(max_heap)
            req_qnty = min(truckSize, qnty)
            qnty -= req_qnty
            truckSize -= req_qnty
            max_units += req_qnty * -units_per_box
            if qnty != 0:
                heapq.heappush(max_heap, [units_per_box, qnty])
        return max_units
                   