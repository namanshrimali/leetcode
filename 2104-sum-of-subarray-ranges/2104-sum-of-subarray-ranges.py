class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        sol, L = 0, len(nums)
        min_stack = []
        
        min_nums = [float('-inf')]+nums+[float('-inf')]
        for i in range(len(min_nums)):
            num = min_nums[i]
            while min_stack and min_nums[min_stack[-1]] > num:
                j = min_stack.pop()
                k = min_stack[-1]
                
                j_min_to_right = i-j
                j_min_to_left = j-k
                
                sol -= min_nums[j]*j_min_to_right*j_min_to_left
            min_stack.append(i)
        max_nums = [inf]+nums+[inf]
        max_stack = []
        for i in range(len(max_nums)):
            num = max_nums[i]
            while max_stack and max_nums[max_stack[-1]] < num:
                j = max_stack.pop()
                k = max_stack[-1]
                
                j_max_to_right = i-j
                j_max_to_left = j-k
                sol += max_nums[j] * j_max_to_right * j_max_to_left
            max_stack.append(i)
        return sol