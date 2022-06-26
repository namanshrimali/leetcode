class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def can_fit_with(given_capacity):
            curr_day, curr_capacity = 0, 0
            
            for i in range(len(weights)):
                curr_capacity += weights[i]
                if curr_capacity > given_capacity:
                    if curr_day == days - 1:
                        return False
                    curr_capacity = weights[i]
                    curr_day += 1
            return True
        
        def binary_search(start, end):
            while start < end:
                mid = (start+end)//2
                if can_fit_with(mid):
                    end = mid
                else:
                    start = mid+1
            return end
        
        min_capacity, max_capacity = 0, 0
        for weight in weights:
            min_capacity = max(min_capacity, weight)
            max_capacity += weight
        
        return binary_search(min_capacity, max_capacity)
        