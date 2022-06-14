class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        arr = [0] + arr
        min_stack = [0]
        n = len(arr)
        min_values = [0] * n
        for i in range(1, n):
            while min_stack and arr[min_stack[-1]] >= arr[i]:
                min_stack.pop()
            j = min_stack[-1]
            min_values[i] = min_values[j] + (i-j)*arr[i]
            min_stack.append(i)
        return sum(min_values) % MOD
        