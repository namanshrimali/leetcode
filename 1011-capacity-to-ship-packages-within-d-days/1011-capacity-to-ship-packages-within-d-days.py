class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        n = len(weights)
        def can_fit_within_days(capacity):
            total, days_spent, i = 0, 0, 0
            while i < n and days_spent < days:
                total += weights[i]
                
                if total > capacity:
                    if days_spent == days - 1:
                        break
                    days_spent += 1
                    total = weights[i]
                i+=1
            return i == n
        start, end = max(weights), sum(weights)
        while start < end:
            mid = (start + end) // 2
            if can_fit_within_days(mid):
                end = mid
            else:
                start = mid + 1
        return end
            