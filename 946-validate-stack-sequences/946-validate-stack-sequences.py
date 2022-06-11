class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        j, n = 0, len(pushed)
        stack = []
        for i in pushed:
            stack.append(i)
            
            while j < n and stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1

        return j == n
