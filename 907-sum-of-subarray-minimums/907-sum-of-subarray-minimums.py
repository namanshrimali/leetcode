class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        L, MOD_VAL = len(arr), 10**9+7
        left_stack, right_stack, sol_arr = [], [], []
        
        def calc_left_max(i):
            # returns the number of values that are strictly greater than or equals to given index i 
            count = 1
            while(left_stack and left_stack[-1][0]>arr[i]):
                _, prev_count = left_stack.pop()
                count+=prev_count
            left_stack.append((arr[i], count))
            return count
        
        def calc_right_max(i):
            # returns the number of values that are strictly greater than or equals to given index i 
            count = 1
            while(right_stack and right_stack[-1][0]>=arr[i]):
                _, prev_count = right_stack.pop()
                count+=prev_count
            right_stack.append((arr[i], count))
            return count
        
        for i in range(L):
            sol_arr.append(calc_left_max(i))
        
        for i in range(L-1, -1, -1):
            sol_arr[i]*= calc_right_max(i)*arr[i]
            
        return sum(sol_arr)%MOD_VAL
            