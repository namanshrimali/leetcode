class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i, j, n = 0, 0, len(pushed)
        while i < n:
            stack.append(pushed[i])
            i += 1
            while stack and j < n and popped[j] == stack[-1]:
                stack.pop()
                j += 1
        return j == n