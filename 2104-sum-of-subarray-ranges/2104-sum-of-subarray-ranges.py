class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        sol, L = 0, len(nums)
        min_stack = []
        
        min_nums = [float('-inf')]+nums+[float('-inf')]
        
        # in the below for loop, we calculate the total number of sub arrays where a number is minimum
        # When we encounter a number that is less than the last number,  we pop out one by one all the numbers in 
        # the min stack which are necessarily greater than the current number. We then calculate the number of 
        # subarrays where those popped number are minimum. Since in min stack, all numbers are necessarily in 
        # increasing order, to calulate number of subarrays on left where popped number is minimum, we subtract the 
        # popped number index with the index on top of min stack. Similarly, we calculate number of subarrays on the 
        # right of popped number in which it is minimum. Since current number is minimum, subarray in the right would 
        # be curr idx - popped idx
        # exactly same logic is used for calculating number of subarrays where number is maximum
        
        
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