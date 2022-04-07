class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda a: a[0])
        stack = []
        for start, end in intervals:
            if stack and stack[-1][0] <= start <= stack[-1][1]:
                stack[-1] = [stack[-1][0], max(end, stack[-1][1])]   
            else:
                stack.append([start, end])
        return stack