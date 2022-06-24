class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [-1] * n
        stack = []
        
        for _ in range(2):
            for i in range(n):
                while stack and nums[stack[-1]] < nums[i]:
                    answer[stack.pop()] = nums[i]
                stack.append(i)
        return answer