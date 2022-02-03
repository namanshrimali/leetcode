class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        sol, current, L = 0, 0, len(height)
        while current < L:
            while stack and height[current]>height[stack[-1]]:
                prev_idx = stack.pop()
                if len(stack)==0:
                    break
                second_prev_idx = stack[-1]
                width = current - second_prev_idx - 1
                depth = min(height[current], height[second_prev_idx])-height[prev_idx]
                sol+= width*depth
            stack.append(current)
            current+=1
        return sol
        