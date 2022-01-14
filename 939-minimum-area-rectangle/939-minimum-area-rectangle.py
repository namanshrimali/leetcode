class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        min_area = float('inf')
        seen = set()
        for x1, y1 in points:
            for x2, y2 in seen:
                if (x1, y2) in seen and (x2, y1) in seen:
                    min_area = min(min_area, abs(x1-x2)*abs(y1-y2))
            seen.add((x1, y1))
        return 0 if min_area == float('inf') else min_area
        