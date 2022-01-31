class Solution:
    def minSwaps(self, data: List[int]) -> int:
        L = len(data)
        total_ones = 0
        zero_count = [0]*(L+1)
        for i in range(L):
            if data[i] == 1:
                total_ones+=1 
                zero_count[i+1] = zero_count[i]
            else:
                zero_count[i+1]= zero_count[i] + 1
        left, right = 0, total_ones-1
        sol = float('inf')
        while right<L:
            sol = min(sol, zero_count[right+1] - zero_count[left])
            left+=1
            right+=1
        return sol
        