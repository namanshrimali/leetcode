class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i, j, n = 0, 0, len(pushed)
        stack = []
        while i < n and j < n:
            while i < n and ( not stack or stack[-1] != popped[j]):
                stack.append(pushed[i])
                i += 1
            while j < n and stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1

        return i == j == n
