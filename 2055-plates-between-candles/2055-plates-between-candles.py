class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        closest_right_candle = [None] * n
        plates_till_candle = [0] * n
        plates_till_now = 0
        
        for i in range(n):
            if s[i] == '|':
                plates_till_candle[i] = plates_till_now
            else:
                if i > 0:
                    plates_till_candle[i] = plates_till_candle[i-1]
                plates_till_now += 1
        
        last_right_candle = n
        for i in range(n-1, -1, -1):
            if s[i] == '|':
                last_right_candle = i
            closest_right_candle[i] = last_right_candle
        result = []
        
        for start_idx, end_candle in queries:
            next_candle = closest_right_candle[start_idx]
            if next_candle <= end_candle:
                start_candle = next_candle
            else:
                start_candle = start_idx
            result.append(plates_till_candle[end_candle] - plates_till_candle[start_candle])
        return result
        