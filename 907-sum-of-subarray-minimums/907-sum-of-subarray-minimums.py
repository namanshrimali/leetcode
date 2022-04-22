class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        total = 0
        
        arr = [0] + arr
        stack = [0]
        n = len(arr)
        result = [0] * n
        for i in range(n):
            while arr[stack[-1]] > arr[i]:
                stack.pop()
            j = stack[-1]
            result[i] = result[j] + (i-j)*arr[i]

            stack.append(i)        
        
        return sum(result) % MOD