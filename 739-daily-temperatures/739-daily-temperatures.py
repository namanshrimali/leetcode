class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        max_temperature = 0
        for curr_idx in range(n-1, -1, -1):
            curr_temperature = temperatures[curr_idx]
            if curr_temperature >= max_temperature:
                max_temperature = curr_temperature
                continue
            days = 1
            while temperatures[curr_idx + days] <= temperatures[curr_idx]:
                days += answer[curr_idx + days]
            answer[curr_idx] = days
        return answer
        