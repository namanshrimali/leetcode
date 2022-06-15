class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temperature_stack = []
        n = len(temperatures)
        answer = [0] * n
        for i in range(n):
            while temperature_stack and temperatures[temperature_stack[-1]] < temperatures[i]:
                j = temperature_stack.pop()
                answer[j] = i - j
            temperature_stack.append(i)
        return answer