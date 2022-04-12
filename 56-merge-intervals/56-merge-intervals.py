class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])
        
        stack = []
        for start, end in intervals:
            if stack and stack[-1][1] >= start:
                stack[-1][1] = max(stack[-1][1], end)
            else:
                stack.append([start, end])
        return stack
        