class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda boxType: boxType[1], reverse = True)
        totalUnitsLoaded = 0
        for total_box, unit_per_box in boxTypes:
            if truckSize == 0:
                break
            boxes_loaded = min(truckSize, total_box)
            totalUnitsLoaded += boxes_loaded * unit_per_box
            truckSize -= boxes_loaded
        return totalUnitsLoaded
        