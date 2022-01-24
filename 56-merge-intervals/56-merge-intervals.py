class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sol = []
        intervals.sort(key=lambda interval:interval[0])
        sol.append([intervals[0][0], intervals[0][1]])
        for start, end in intervals[1:]:
            last_start, last_end = sol[-1]
            if start <= last_end:
                sol[-1][0] = min(last_start, start)
                sol[-1][1] = max(last_end, end)
            else:
                sol.append([start, end])
        return sol