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
        i = 0
        sol = float('inf')
        while i+total_ones-1<L:
            sol = min(sol, zero_count[i+total_ones] - zero_count[i])
            i+=1
        return sol
        