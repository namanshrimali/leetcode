class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        max_temperature = 0
        for curr_day in range(n-1, -1, -1):
            if max_temperature <= temperatures[curr_day]:
                max_temperature = temperatures[curr_day]
                continue
            days = 1
            while temperatures[curr_day + days] <= temperatures[curr_day]:
                days += answer[curr_day + days]
            answer[curr_day] = days
        return answer